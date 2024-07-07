"""
Main Routes Module

This module defines the routes and view functions for general features of the PersonalBlogWebApp
that are not specific to any particular user.

Dependencies:
- flask: For creating routes and handling HTTP requests
- PersonalBlogWebApp.main.forms: For the search form
- PersonalBlogWebApp.models: For the Post model
- flask_login: For accessing the current user

Routes:
    /: Home page
    /home: Alternative route for home page
    /search: Search functionality for posts
    /announcements: Announcements page
    /dev: About the developer page
    /Landing-Page: About the project page

Each route is associated with a view function that handles the logic for that particular endpoint.
"""

from flask import render_template, request, Blueprint
from PersonalBlogWebApp.main.forms import SearchForm
from PersonalBlogWebApp.models import Post
from flask_login import current_user

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    """
    Render the home page.

    Displays a paginated list of all non-scheduled posts, ordered by date posted (descending).
    """
    page = request.args.get('page', 1, type=int)
    posts = Post.query.filter(Post.date_scheduled == None).order_by(
        Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)


@main.route("/search", methods=['GET', 'POST'])
def search():
    """
    Handle the search functionality.

    GET: Render the search form
    POST: Process the search query and display results
    
    This function handles three scenarios:
    1. Initial search query submission
    2. Pagination of search results
    3. Initial rendering of the search page
    """
    form = SearchForm()
    # case when user enters a search keyword that is valid
    if form.validate_on_submit():
        keyword = form.Search.data
        # page number will be by default 1
        page = request.args.get('page', 1, type=int)
        # query the database to find posts that it's content has the searched keywords
        # and return a paginate object with only 5 posts arranged desc by date posted
        posts = Post.query.filter(Post.date_scheduled == None).filter(Post.content.ilike('%' + keyword + '%')).order_by(
            Post.date_posted.desc()).paginate(page=page, per_page=5)
        """ send the searched keyword as a variable to the template to be able to pass it
        to the view function again as a query string so in case of requesting the other pages
        the form is not submitted again so form.Search.data is None so use the value of the keyword query string
        to query the database to get the requested page"""
        return render_template('search.html', title='Search', form=form, posts=posts, keyword=keyword)
    # case when navigating the pages of result of search
    elif request.args.get('page', 1, type=int) and request.args.get('keyword', type=str):
        page = request.args.get('page', 1, type=int)
        keyword = request.args.get('keyword', type=str)
        posts = Post.query.filter(Post.content.ilike('%' + keyword + '%')).order_by(
            Post.date_posted.desc()).paginate(page=page, per_page=5)
        return render_template('search.html', title='Search', form=form, posts=posts, keyword=keyword)
    # case when user request the search route
    return render_template('search.html', title='Search', form=form, posts=None)

@main.route("/announcements")
def announcements():
    """Render the announcements page."""
    return render_template('announcements.html', title="Announcements")

@main.route("/dev")
def dev():
    """Render the about developer page."""
    return  render_template('dev.html', title="About Developer")

@main.route("/Landing-Page")
def About_project():
    """
    Render the landing page / about project page.
    
    This page includes information about the application and considers the current user's authentication status.
    """
    return  render_template('landing_page.html', title="About App", current_user=current_user)
