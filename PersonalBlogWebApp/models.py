"""
Database Models Module

This module defines the database models for the PersonalBlogWebApp using SQLAlchemy ORM.

Dependencies:
- flask: For accessing the current application context
- flask_login: For user authentication functionality
- itsdangerous: For generating and verifying tokens
- datetime: For handling date and time
- PersonalBlogWebApp: For database and login manager instances

Classes:
    User: Represents a user in the application
    Post: Represents a blog post in the application

Functions:
    load_user: User loader function for Flask-Login

This module establishes the structure of the database tables and their relationships,
as well as provides methods for user authentication and token handling.
"""
from flask import current_app
from PersonalBlogWebApp import db, login_manager
from datetime import datetime
from flask_login import UserMixin
from itsdangerous.serializer import Serializer
from os import urandom
TOKEN_EXPIRATION = 100000
salt = urandom(16)


@login_manager.user_loader
def load_user(user_id):
    """
    Flask-Login user loader function.

    Args:
        user_id (int): The user's ID

    Returns:
        User: The User object corresponding to the given user_id
    """
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    """
    User model representing registered users in the application.

    Attributes:
        id (int): Unique identifier for the user
        username (str): User's chosen username
        email (str): User's email address
        image_file (str): Filename of the user's profile picture
        password (str): Hashed password of the user
        posts (relationship): Relationship to user's posts

    Methods:
        get_reset_token: Generates a password reset token
        verify_reset_token: Verifies a password reset token
        __repr__: String representation of the User object
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False,
                           default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author',
                            lazy=True, cascade='all, delete-orphan')

    def get_reset_token(self, expiretime=TOKEN_EXPIRATION):
        """
        Generate a password reset token for the user.

        Args:
            expiretime (int): Token expiration time in seconds

        Returns:
            str: Generated token

        This is an instance method, it takes self as argument which refers to the instance of the class (a specific user object).
        It has access to the data of the class instace so it can uses id to create a unique token based on user id
        """
        s = Serializer(current_app.config['SECRET_KEY'], expiretime)
        data = {'user_id': self.id}
        token = s.dumps(data, salt=salt)
        return token

    @staticmethod
    def verify_reset_token(token):
        """
        Verify a password reset token.

        Args:
            token (str): The token to verify

        Returns:
            User: The user associated with the token if valid, else None

        This is an instance method, it takes self as argument which refers to the instance of the class (a specific user object).
        It has access to the data of the class instace so it can uses id to create a unique token based on user id
        """
        s = Serializer(current_app.config['SECRET_KEY'], TOKEN_EXPIRATION)
        try:
            data = s.loads(token, salt=salt)
            user_id = data['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    """
    Post model representing blog posts in the application.

    Attributes:
        id (int): Unique identifier for the post
        title (str): Title of the post
        date_posted (datetime): Date and time when the post was created
        date_scheduled (datetime): Date and time when the post is scheduled to be published
        content (str): Content of the post
        user_id (int): ID of the user who authored the post

    Methods:
        __repr__: String representation of the Post object
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    date_scheduled = db.Column(db.DateTime, nullable=True, default=None)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
