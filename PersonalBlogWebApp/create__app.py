"""
Application Factory Module

This module contains the create_app function, which serves as a factory for creating
and configuring the Flask application instance.

Dependencies:
- flask: For creating the Flask application
- PersonalBlogWebApp.config: Provides the Configuration class
- PersonalBlogWebApp: Provides various extensions (db, bcrypt, login_manager, mail, scheduler)
- PersonalBlogWebApp.scheduler: Provides the schedule_posts function

Functions:
    create_app(config_class=Configuration): Creates and configures a Flask application instance
"""

from flask import Flask
from PersonalBlogWebApp.config import Configuration
from PersonalBlogWebApp import db, bcrypt, login_manager, mail, scheduler
from PersonalBlogWebApp.scheduler import schedule_posts


def create_app(config_class=Configuration):
    """
    Create and configure an instance of the Flask application.

    This function follows the application factory pattern. It initializes the Flask app,
    sets up configuration, initializes extensions, sets up scheduled tasks, and registers blueprints.

    Args:
        config_class (class, optional): The configuration class to use. Defaults to Configuration.

    Returns:
        Flask: A configured Flask application instance.

    It's Fuction:
        - Initializes database, bcrypt, login manager, mail, and scheduler extensions
        - Starts a scheduled task for post scheduling
        - Registers blueprints for different parts of the application
    """
    # Create Flask app instance
    app = Flask(__name__)

    # Load configuration
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    scheduler.init_app(app)

    # Set up scheduled task
    @scheduler.task('interval', id='schedule_posts', seconds=60)
    def scheduled_task():
        schedule_posts(app)

    # Start the scheduler
    scheduler.start()

    # Import and register blueprints
    from PersonalBlogWebApp.users.routes import users
    from PersonalBlogWebApp.posts.routes import posts
    from PersonalBlogWebApp.main.routes import main
    from PersonalBlogWebApp.errors.handlers import errors

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app
