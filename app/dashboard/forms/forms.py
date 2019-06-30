from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField

# login and registration


class UserForm(FlaskForm):
    email = TextField('email', id='email_login')
    confirm_email = TextField('c_email', id='c_email_login')
    password = PasswordField('Password', id='pwd')
    repeat_password = PasswordField('r_Password', id='r_pwd')
    first_name = TextField('first_name', id='first_name')
    first_name = TextField('last_name', id='last_name')
    role = TextField('role', id='role')


class CreateAccountForm(FlaskForm):
    username = TextField('Username', id='username_create')
    email = TextField('Email', id='email_create')
    password = PasswordField('Password', id='pwd_create')
