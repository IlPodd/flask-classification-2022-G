from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField
from wtforms.validators import DataRequired
from app.utils.list_images import list_images


class HistogramForm(FlaskForm):
    """I extend the FlaskForm class which provides an alternative to web forms by creating a form class in the application, implementing the fields in the template and handling the return data in the application.
WTForms also uses a CSRF token to provide protection against CSRF attacks"""
    image = SelectField('image', choices=list_images(), validators=[DataRequired()])
    submit = SubmitField('Submit')