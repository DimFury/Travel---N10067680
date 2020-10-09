from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, SubmitField, StringField, PasswordField
from wtforms.validators import InputRequired, Length, Email, EqualTo



class DestinationForm(FlaskForm):
    name = StringField('Country', validators=[InputRequired('Country is required')])
    image = StringField('Image', validators=[InputRequired('Image is required')])
    description = StringField('Description', validators=[InputRequired('Description is required'),
                                                        Length(min=10, max=300, message='Description is too short or too long')])
    currency = StringField('Currency', validators=[InputRequired('Currency is required')])


    submit = SubmitField('Create')


class LoginForm(FlaskForm):
    user_name = StringField('User Name', validators=[InputRequired('User Name is required')])
    password = PasswordField('Password', validators=[InputRequired('Password Name is required')])
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    user_name = StringField('User Name', validators=[InputRequired('User Name is required')])
    email = StringField('Email', validators=[InputRequired('Email is required'), Email('Email is not valid')])

    password = PasswordField('Password', validators=[InputRequired('Password Name is required')])
    confirm_password = PasswordField('Confirm Password', validators=[EqualTo('password', message='Passwords do not match')])

    submit = SubmitField('Register')

class CommentForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[InputRequired('Comment Is Required'), Length(min=5, max=400, message='Comment is too long or too short')])
    submit = SubmitField('Add Comment')