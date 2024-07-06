"""
Configuration Module

This module loads configuration settings from a JSON file stored on server 
and defines a Configuration class to store these settings for use in the application.

Dependencies:
- json: Used to parse the JSON configuration file.

Classes:
    Configuration: Stores application configuration settings.
    
"""

import json

# Load configuration from JSON file
with open('/home/ubuntu/etc/ALX-SWE-Portfolio-Project-config.json') as f:
    config_json = json.load(f)


class Configuration:
    """
    Configuration class to store application settings.

    Attributes:
        SECRET_KEY (str): A secret key used for cryptographic signing in the application.
        SQLALCHEMY_DATABASE_URI (str): The URI for the SQLAlchemy database connection.
        MAIL_SERVER (str): The SMTP server address for sending emails.
        MAIL_PORT (int): The port number for the SMTP server.
        MAIL_USERNAME (str): The username for authenticating with the SMTP server.
        MAIL_PASSWORD (str): The password for authenticating with the SMTP server.
        MAIL_USE_TLS (bool): Whether to use TLS when connecting to the SMTP server.

    All attributes are loaded from the JSON configuration file, except for MAIL_USE_TLS
    which is hardcoded to True.
    """

    # Secret key for the app used in serialization, encryption, signing data
    SECRET_KEY = config_json.get('SECRET_KEY')

    # SQLAlchemy database URI
    SQLALCHEMY_DATABASE_URI = config_json.get('SQLALCHEMY_DATABASE_URI')

    # SMTP client configuration
    MAIL_SERVER = config_json.get('MAIL_SERVER')
    MAIL_PORT = config_json.get('MAIL_PORT')
    MAIL_USERNAME = config_json.get('MAIL_USERNAME')
    MAIL_PASSWORD = config_json.get('MAIL_PASSWORD')
    MAIL_USE_TLS = True
