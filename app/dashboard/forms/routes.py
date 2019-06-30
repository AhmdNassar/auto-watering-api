from app.dashboard.forms import blueprint
from flask import render_template, redirect, url_for, request
from flask_login import login_required
import datetime

from app.api.model.user import User
from app import db


@blueprint.route('/<template>')
@login_required
def route_template(template):
    return render_template(template + '.html')


@blueprint.route('/newuser', methods=['POST', 'GET'])
@login_required
def newUser():
    signup_form = request.form
    username = signup_form['name'] + ' ' + signup_form['name2']
    email = signup_form['email']
    phone = signup_form['number']
    password = signup_form['password']
    user = User.query.filter_by(email=email).first()
    if user:
        return 'user already exist.\nplease back again!'
    registered_on = datetime.datetime.utcnow()
    user = User(email=email, password=password,
                username=username, registered_on=registered_on, phone=phone)
    db.session.add(user)
    db.session.commit()

    return redirect(url_for('forms_blueprint.route_template', template='user'))


@blueprint.route('/newadmin', methods=['POST', 'GET'])
@login_required
def newAdmin():
    signup_form = request.form
    username = signup_form['name'] + ' ' + signup_form['name2']
    email = signup_form['email']
    phone = signup_form['number']
    password = signup_form['password']
    role = 'admin'
    user = User.query.filter_by(email=email).first()
    if user:
        return 'admin already exist.\nplease back again!'
    registered_on = datetime.datetime.utcnow()
    user = User(email=email, password=password,
                username=username, registered_on=registered_on, phone=phone, role=role)
    db.session.add(user)
    db.session.commit()

    return redirect(url_for('forms_blueprint.route_template', template='admin'))
