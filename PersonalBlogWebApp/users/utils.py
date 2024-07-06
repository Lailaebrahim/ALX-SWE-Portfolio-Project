"""
User Utility Functions Module

This module contains utility functions for handling various operations related to user 
profile management and password reset functionality.

Dependencies:
- secrets: For generating secure random tokens
- os: For file and path operations
- PIL: For image processing
- flask: For accessing the current application context and generating URLs
- flask_login: For accessing the current user
- flask_mail: For sending emails

Functions:
    savr_pic: Saves and processes user profile pictures
    delete_pic: Deletes a user's profile picture
    send_reset_email: Sends a password reset email to a user
    
"""

import secrets
import os
from PIL import Image
from flask import url_for, current_app
from PersonalBlogWebApp import mail
from flask_login import current_user
from flask_mail import Message



def savr_pic(form_profile_pic):
    """
    Save and process a user's profile picture.

    Args:
        form_profile_pic: uploaded user image

    Returns:
        str: The filename of the saved image

    This function generates a unique filename, resizes the image,
    saves it to the appropriate directory, and delete old profile picture.
    """
    
    # creating a random hex token to name the image so paths saved in DB don't repeat
    random_hex = secrets.token_hex(8)
    # using os.path methods to get the extension of the uploaded image
    _, fext = os.path.splitext(form_profile_pic.filename)
    # profile picture file name is the generated random hex token and the extension
    pic_name = random_hex + fext
    # creating the full path of the profile picture, so it can be used to be rendered by templates
    pic_path = os.path.join(current_app
                            .root_path, 'static/profile_pics', pic_name)
    # Resizing image so it want to take up much space
    input_size = (125, 125)
    i = Image.open(form_profile_pic)
    i.thumbnail(input_size)
    i.save(pic_path)
    if current_user.image_file is not None and current_user.image_file != 'default.jpg':
        # deleting the old image from the static folder
        os.remove(os.path.join(current_app
                               .root_path, 'static/profile_pics', current_user.image_file))
    return pic_name

def delete_pic(user):
    """
    Delete a user's profile picture.

    Args:
        user: User object whose profile picture is to be deleted

    This function removes the user's profile picture from the static/profile_pics directory
    if it exists and is not the default image.
    """
    if user.image_file != None and user.image_file != 'default.jpg':
        os.remove(os.path.join(current_app
                               .root_path, 'static/profile_pics', user.image_file))

def send_reset_email(user):
    """
    Send a password reset email to a user.

    Args:
        user: User object to whom the reset email will be sent

    This function generates a password reset token, creates an email message
    with a reset link, and sends it to the user's email address.
    """
    token = user.get_reset_token()
    msg = Message('Password Reset', recipients=[
                  user.email], sender='lailaebrahimtawfik@gmail.com')
    msg.body = f"To Reset Your Password visit the following link {url_for('users.reset_password', token=token, _external=True)}"
    mail.send(msg)
