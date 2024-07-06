"""
Post Scheduling Module

This module contains a function to automatically publish scheduled blog posts.

Dependencies:
- PersonalBlogWebApp.models: Provides the Post model
- PersonalBlogWebApp: Provides the db object for database operations
- datetime: Used for handling date and time operations

Functions:
    schedule_posts(app): Publishes posts that have reached their scheduled date and time.

"""

from PersonalBlogWebApp.models import Post
from PersonalBlogWebApp import db
from datetime import datetime


def schedule_posts(app):
    """
    Publishes posts that have reached their scheduled date and time.

    This function is designed to be run periodically by an APScheduler instance.
    It checks for any posts with a scheduled date that has passed and marks them as published
    by setting their date_scheduled to None.

    Args:
        app: The Flask application instance. This is needed to create an application context.

    Behavior:
        1. Creates an application context.
        2. Queries the database for posts with a scheduled date in the past.
        3. For each such post, sets date_scheduled to None and commits the change.
        4. If any error occurs during the process, it prints an error message.

    Error Handling:
        Catches and prints any exceptions that occur during execution to prevent the scheduler from crashing.
    """
    with app.app_context():
        try:
            now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
            posts = Post.query.filter(Post.date_scheduled <= now).all()
            for post in posts:
                post.date_scheduled = None
                db.session.commit()
        except Exception as e:
            print("Error running schedule_posts job: %s", e)
