"""
Main Forms Module

This module defines the form used for search functionality in the PersonalBlogWebApp.

Dependencies:
- flask_wtf: For creating Flask  forms
- wtforms: For defining form fields and validators

Classes:
    SearchForm: Form for search functionality
"""

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class SearchForm(FlaskForm):
    """
    Form for search functionality.

    This form is used to capture user input for searching blog posts.

    Attributes:
        Search (StringField): The search input field
            validators:
                - DataRequired: Ensures the field is not empty
                - Length: Ensures the search query is between 2 and 200 characters
        submit (SubmitField): The submit button for the form

    Usage:
        This form is typically rendered in templates and processed in route handlers
        to perform search operations on blog posts.
    """
    Search = StringField("Search", validators=[
        DataRequired(), Length(min=2, max=200)])
    submit = SubmitField('Search')
