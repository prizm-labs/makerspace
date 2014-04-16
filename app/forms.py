"""
Contains Forms
"""

from flask_wtf import Form
from wtforms import TextField, PasswordField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, EqualTo


class LoginForm(Form):
    """
    User Log In Form.
    Please add proper validators to the fields used.
    """
    username = TextField('Username')
    email = TextField('Email')
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')

class SubscribeForm(Form):
    """
    Email collector
    """
    email = TextField('Email', validators=[DataRequired()])



class RegisterForm(Form):
    """
    User Register Form.
    Please add proper validators to the fields used.
    """
    first_name = TextField('First Name')
    last_name = TextField('Last Name')
    username = TextField('Username')
    email = TextField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField(
        'Confirm Password',
        validators=[
            DataRequired(),
            EqualTo('password', message='Passwords must match')
        ])
    tc_accept = BooleanField('I read Terms and Conditions')


class ContactForm(Form):
    """
    Contact Form.
    """
    name = TextField('Name')
    email = TextField('Email', validators=[DataRequired()])
    message = TextAreaField('Message', validators=[DataRequired()])


class BlogCommentForm(Form):
    """
    Blog Comment Form.
    """
    name = TextField('Name', validators=[DataRequired()])
    email = TextField('Email')
    message = TextAreaField('Message', validators=[DataRequired()])


class NewsletterSubscriptionForm(Form):
    """
    Footer Newsletter Subscription Form.
    """
    email = TextField('Email Address', validators=[DataRequired()])
