"""
Forms for Post Management

This file defines the form used for creating and editing blog posts.

Dependencies:
- flask_wtf: For creating forms
- wtforms: For form fields and validators

Classes:
    PostForm: Form for creating and editing blog posts
"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class PostForm(FlaskForm):
    """
    Form for creating and editing blog posts.

    Fields:
        title (StringField): The title of the post
        content (TextAreaField): The content of the post
        submit (SubmitField): Button to submit the form
    """
    title = StringField("Title", validators=[
                        DataRequired(), Length(min=10, max=100)])
    content = TextAreaField("Content", validators=[DataRequired()])
    submit = SubmitField('Post')
