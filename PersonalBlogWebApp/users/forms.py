"""
User Forms Module

This module defines various form classes used in the PersonalBlogWebApp for user input handling and validation.

Dependencies:
- flask_wtf: For creating Flask-specific forms
- flask_wtf.file: For handling file uploads
- wtforms: For defining form fields and validators
- PersonalBlogWebApp.models: Provides the User model for database queries
- flask_login: Provides current_user for accessing the logged-in user

Classes:
    RegistrationForm: Form for user registration
    LoginForm: Form for user login
    UpdateAccountForm: Form for updating user account information
    ResetPasswordRequest: Form for requesting a password reset
    ResetPassword: Form for resetting the password

Each form class inherits from FlaskForm and defines various fields with appropriate validators.
Custom validation methods are included where necessary to check for unique usernames and emails.
"""

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from PersonalBlogWebApp.models import User
from flask_login import current_user


class RegistrationForm(FlaskForm):
    """
    Form for user registration.

    Fields:
        username (StringField): User's chosen username
        email (StringField): User's email address
        password (PasswordField): User's chosen password
        confirm_password (PasswordField): Password confirmation
        submit (SubmitField): Form submission button

    Methods:
        validate_username: Ensures the username is not already taken
        validate_email: Ensures the email is not already registered
    """
    username = StringField('Username', validators=[
                           Length(min=2, max=20), DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[
                                     DataRequired(), EqualTo('password')])
    submit = SubmitField("Sign Up")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(
                "This username is taken. Please choose another one!")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(
                "This email already have an account. Please choose another one or Login to your account")


class LoginForm(FlaskForm):
    """
    Form for user login.

    Fields:
        email (StringField): User's email address
        password (PasswordField): User's password
        remember (BooleanField): Option to remember user's session
        submit (SubmitField): Form submission button
    """
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField('Remember Me?')
    submit = SubmitField("Login")


class UpdateAccountForm(FlaskForm):
    """
    Form for updating user account information.

    Fields:
        username (StringField): User's new username
        email (StringField): User's new email address
        profile_pic (FileField): User's new profile picture
        submit (SubmitField): Form submission button

    Methods:
        validate_username: Ensures the new username is not same as old
        validate_email: Ensures the new email is not same as old
    """
    username = StringField('Username', validators=[
                           Length(min=2, max=20), DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    profile_pic = FileField("Update Your Profile Picture", validators=[
                            FileAllowed(['jpg', 'png'])])
    submit = SubmitField("Update")

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError(
                    "This username is taken. Please choose another one.")

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError(
                    "This email is taken. Please choose another one.")


class ResetPasswordRequest(FlaskForm):
    """
    Form for requesting a password reset.

    Fields:
        email (StringField): User's registered email address
        submit (SubmitField): Form submission button

    Methods:
        validate_email: Ensures the email is associated with an existing account
    """
    email = StringField("Email", validators=[DataRequired(), Email()])
    submit = SubmitField("Request Password Reset")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError(
                "This email doesn't have an account. Please registser first.")


class ResetPassword(FlaskForm):
    """
    Form for resetting the user's password.

    Fields:
        password (PasswordField): User's new password
        confirm_password (PasswordField): New password confirmation
        submit (SubmitField): Form submission button
    """
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[
                                     DataRequired(), EqualTo('password')])
    submit = SubmitField("Reset Password")
