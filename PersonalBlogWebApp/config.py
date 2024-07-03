import os
import json

# Load configuration from JSON file
with open('/home/ubuntu/etc/ALX-SWE-Portfolio-Project-config.json') as f:
    config_json = json.load(f)


class Configuration:
    # define a secret key for the app used in serialization, encryption, signing data
    SECRET_KEY = config_json.get('SECRET_KEY')

    # The SQLALCHEMY_DATABASE_URI configuration variable is used to specify the database URI for SQLAlchemy
    SQLALCHEMY_DATABASE_URI = config_json.get('SQLALCHEMY_DATABASE_URI')

    # adding configuration for the SMTP client to be able to connect to the SMTP server defined in the MAIL_SERVER
    MAIL_SERVER = config_json.get('MAIL_SERVER')
    MAIL_PORT = config_json.get('MAIL_PORT')
    MAIL_USERNAME = config_json.get('MAIL_USERNAME')
    MAIL_PASSWORD = config_json.get('MAIL_PASSWORD')
    MAIL_USE_TLS = True

