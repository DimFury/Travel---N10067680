from flask import Blueprint, session, redirect, url_for, render_template
from .models import authentication_blueprint,Comment
from Travel.forms import LoginForm


authentication_blueprint = Blueprint('authentication', __name__, url_prefix='/authentication')

@authentication_blueprint.route('/login', Methods=['GET', 'POST'])
def login():
    login_form_instance = LoginForm()

    if login_form_instance.validate_on_submit():
        return redirect(url_for('authentication.login'))
    
    return render_template('authentication/login.html', form=login_form_instance)

@authentication_blueprint.route('/register', Methods=['GET', 'POST'])
def login():
    return ""


@authentication_blueprint.route('/logout')
def login():
    session.clear()
    return ""