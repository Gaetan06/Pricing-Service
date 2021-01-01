from flask import Blueprint, render_template, request, session, redirect, url_for
from models.user import User, UserErrors

user_blueprint = Blueprint('users', __name__)


@user_blueprint.route('/register', methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':
        user_name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        try:
            User.register_user(user_name, email, password)
            session['email'] = email
            session['user_name'] = user_name
            return render_template('home.html')
        except UserErrors.UserError as e:
            return e.message

    return render_template('users/register.html')


@user_blueprint.route('/login', methods=['GET', 'POST'])
def login_user():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            if User.is_login_valid(email, password):
                user = User.find_one_by('email', email)
                session['email'] = user.email
                session['name'] = user.name
                return render_template('home.html')
        except UserErrors.UserError as e:
            return e.message

    return render_template('users/login.html')


@user_blueprint.route('/logout')
def logout_user():
    session['email'] = None
    return redirect(url_for('.login_user'))

