"""
Error Handlers Module

This module defines custom error handlers for the PersonalBlogWebApp.
It uses Flask's error handling mechanism to provide user-friendly error pages.

Dependencies:
- flask: For creating routes and rendering templates

Error codes handled:
- 403: Forbidden
- 404: Not Found
- 500: Internal Server Error

"""

from flask import Blueprint, render_template


errors = Blueprint('errors', __name__)


@errors.app_errorhandler(403)
def error_403(error):
    """
    Handle 403 Forbidden errors.

    Args:
        error: The error object passed by Flask

    Returns:
        tuple: A tuple containing the rendered template and the 403 status code
    """
    return render_template('errors/403.html'), 403


@errors.app_errorhandler(404)
def error_404(error):
    """
    Handle 404 Not Found errors.

    Args:
        error: The error object passed by Flask

    Returns:
        tuple: A tuple containing the rendered template and the 404 status code
    """
    return render_template('errors/404.html'), 404


@errors.app_errorhandler(500)
def error_500(error):
    """
    Handle 500 Internal Server Error.

    Args:
        error: The error object passed by Flask

    Returns:
        tuple: A tuple containing the rendered template and the 500 status code
    """
    return render_template('errors/500.html'), 500
