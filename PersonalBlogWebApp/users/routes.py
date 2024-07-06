"""
User Routes Module

This module defines the routes and view functions related to user management in the PersonalBlogWebApp.

Dependencies:
- flask: For creating routes and handling HTTP requests
- flask_login: For user authentication and session management
- PersonalBlogWebApp: For database models, forms, and utility functions

Routes:
    - /register: User registration
    - /login: User login
    - /logout: User logout
    - /account: User account management
    - /user/<username>: Display user's posts
    - /reset_password: Password reset request
    - /reset_password/<token>: Password reset with token
    - /user/<user_id>/delete: Delete user account

Each route is associated with a view function that handles the logic for that particular endpoint.
"""

from PersonalBlogWebApp import db, bcrypt
from flask import render_template, url_for, flash, redirect, request, Blueprint, abort, session
from flask_login import login_user, current_user, logout_user, login_required
from PersonalBlogWebApp.models import User, Post
from PersonalBlogWebApp.users.forms import RegistrationForm, LoginForm, UpdateAccountForm, ResetPasswordRequest, ResetPassword
from PersonalBlogWebApp.users.utils import savr_pic, send_reset_email, delete_pic

users = Blueprint('users', __name__)


@users.route("/register", methods=['GET', 'POST'])
def register():
    """
    Handle user registration.

    GET: Render registration form
    POST: Process form submission, create new user if valid
    """
    # current_user: This is a special variable provided by Flask-Login that always contains the current logged-in user.
    if current_user.is_authenticated:
        # if current user to app is logged in then redirect him to home page
        return redirect(url_for('users.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        # if form is valid hash entered password
        hashed_pwd = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        # create new user with form data and hashed password
        user = User(username=form.username.data,
                    email=form.email.data, password=hashed_pwd)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created successfully! Login to access your account.', 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html', title='Register', form=form)


@users.route("/login", methods=['GET', 'POST'])
def login():
    """
    Handle user login.

    GET: Render login form
    POST: Authenticate user and log them in if credentials are valid
    """
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            # login_user: This function is used to log in a user by associating a user object with the current session.
            login_user(user, remember=form.remember.data)
            # this view is the redirection when user try to access a page needs authentication so using next query string it redirects user after login back to the page he requested.
            next_route = request.args.get('next')
            if next_route != None:
                return redirect(next_route)
            else:
                return redirect(url_for('main.home'))
        else:
            flash(f"Unsuccessful login! Please check email and password.", 'danger')
    return render_template('login.html', title='login', form=form)


@users.route("/logout")
def logout():
    """Log out the current user, clear their session and redirect to home page."""
    logout_user()
    return redirect(url_for('main.home'))


@users.route("/account", methods=['GET', 'POST'])
# login_required: This is a decorator that can be used to protect views from being accessed by unauthenticated users.
# When users request this route it will redirect the user to the login page if they are not currently logged in.
@login_required
def account():
    """
    Handle user account management.

    GET: Display user account information
    POST: Update user account information
    """
    form = UpdateAccountForm()
    if form.validate_on_submit():
        # if form is valid and the user submitted a profile picture then call saver method
        # which saves the images and create the full path for it
        if form.profile_pic.data:
            pic_name = savr_pic(form.profile_pic.data)
            # then save that path to the current user image file field
            current_user.image_file = pic_name
        current_user.username = form.username.data
        current_user.email = form.email.data
        # commit changes to be saved in th DB
        db.session.commit()
        flash(f'Your account has been updated successfully!', 'success')
        return redirect(url_for('users.account'))
    # if user pressed on my account on the navigation bar which sends a GET request for that url
    elif request.method == 'GET':
        # then value of form fields will be the current values of the logged-in user
        form.username.data = current_user.username
        form.email.data = current_user.email
    # rendering the account.html template with the form values and the current user image file path
    image_file = url_for(
        'static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Your Account', image_file=image_file, form=form)


@users.route("/user/string:<username>")
def user_posts(username):
    """Display posts for a specific user."""
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user).filter(Post.date_scheduled == None).order_by(
        Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('user_posts.html', posts=posts, user=user)


@users.route("/reset_password", methods=['POST', 'GET'])
def reset_password_request():
    """
    Handle password reset requests.

    GET: Render password reset request form
    POST: Process reset request and send reset email
    """
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = ResetPasswordRequest()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        # No need to check if user is None here as in form a custom validator defined to do this
        send_reset_email(user)
        flash('an email has been sent to you with the instructions to reset your password.', 'info')
        return redirect(url_for('users.login'))
    return render_template('reset_password_request.html', title='Reset Password', form=form)


@users.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_password(token):
    """
    Handle password reset with token.

    GET: Verify reset token and render password reset form
    POST: Process new password and update user's password
    """
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    # Only verify the token for GET requests
    if request.method == 'GET':
        user = User.verify_reset_token(token)
        if user is None:
            flash('That is an invalid or expired token', 'warning')
            return redirect(url_for('users.reset_password_request'))
        # Store the user_id in session
        session['reset_user_id'] = user.id
        session.modified = True

    # For POST requests, get the user from the session
    elif request.method == 'POST':
        user_id = session.get('reset_user_id')
        if not user_id:
            flash('Reset session expired. Please try again.', 'warning')
            return redirect(url_for('users.reset_password_request'))
        user = User.query.get(user_id)
        if not user:
            flash('User not found. Please try again.', 'warning')
            return redirect(url_for('users.reset_password_request'))

    form = ResetPassword()
    if form.validate_on_submit():
        user.password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        db.session.commit()
        # Clear the session
        session.pop('reset_user_id', None)
        session.modified = True
        flash('Your password has been updated! You are now able to log in', 'success')
        return redirect(url_for('users.login'))

    return render_template('reset_password.html', title='Reset Password', form=form)


@users.route("/user/<int:user_id>/delete", methods=['GET', 'POST'])
@login_required
def delete_account(user_id):
    """Delete user account and associated data."""
    user = User.query.get_or_404(user_id)
    if user.id != current_user.id:
        abort(403)
    logout_user()
    delete_pic(user)
    db.session.delete(user)
    db.session.commit()
    flash('Your account has been deleted successfully!', 'success')
    return redirect(url_for('main.home'))
