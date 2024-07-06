"""
PersonalBlogWebApp Initialization Module

This module initializes core components and extensions for the PersonalBlogWebApp.

Extensions:
    - SQLAlchemy: For database ORM
    - Bcrypt: For password hashing
    - LoginManager: For user session management
    - Mail: For email functionality
    - APScheduler: For task scheduling

Each extension is instantiated here to be later initialized with the application
in the application factory.

Attributes:
    db (SQLAlchemy): Database ORM instance
    bcrypt (Bcrypt): Password hashing utility
    login_manager (LoginManager): User session management utility
    mail (Mail): Email sending utility
    scheduler (APScheduler): Task scheduling utility
"""

from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_apscheduler import APScheduler

# Database ORM
db = SQLAlchemy()

# Password hashing utility
bcrypt = Bcrypt()

# User session management
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

# Email functionality
mail = Mail()

# Task scheduling
scheduler = APScheduler()
