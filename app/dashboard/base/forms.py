from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField

# login and registration


class LoginForm(FlaskForm):
    email = TextField('email', id='email_login')
    password = PasswordField('Password', id='pwd_login')


class CreateAccountForm(FlaskForm):
    username = TextField('Username', id='username_create')
    email = TextField('Email', id='email_create')
    password = PasswordField('Password', id='pwd_create')
