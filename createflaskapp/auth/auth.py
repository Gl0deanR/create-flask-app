from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from createflaskapp import db
from createflaskapp.models import User

auth = Blueprint('auth', __name__,
                 url_prefix='/auth',
                 template_folder='templates',
                 static_folder='static')


@auth.route('/register', methods=['GET', 'POST'])
def register_page():
    if request.method == 'GET':
        return render_template('auth/register.html')

    if request.method == 'POST':
        if request.form.get('username') == "" or request.form.get('email_address') == "" or request.form.get(
                'last_name') == "" or request.form.get('first_name') == "" or request.form.get('password') == "":
            flash("All fields must be filled in!", category='success')
            return redirect(url_for('auth.register_page'))

        user = User.query.filter_by(email_address=request.form.get('email_address')).first()
        if user is None:
            # Hash the password
            hashed_pw = generate_password_hash(request.form.get('password'), "scrypt")
            user_to_create = User(
                username=request.form.get('username'),
                last_name=request.form.get('last_name'),
                first_name=request.form.get('first_name'),
                email_address=request.form.get('email_address'),
                password_hash=hashed_pw
            )
            db.session.add(user_to_create)
            db.session.commit()

            flash("Your account was created!", category='success')
            return redirect(url_for('auth.login_page'))

        else:
            flash("User already exists!", category='success')
            return redirect(url_for('auth.login_page'))

    return render_template('auth/register.html')


@auth.route('/login', methods=['GET', 'POST'])
def login_page():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard.home'))
    if request.method == 'POST':
        attempted_user = User.query.filter_by(email_address=request.form.get('email_address')).first()
        if attempted_user:
            # Checking the hash password
            if check_password_hash(attempted_user.password_hash, request.form.get('password')):
                login_user(attempted_user)
                flash(f'Successfully logged in as {attempted_user.username}', category='success')
                return redirect(url_for('dashboard.home'))
            else:
                flash('Email and password do not match, please try again.', category='danger')
                return redirect(url_for('auth.login_page'))
        else:
            flash('User does not exist.', category='danger')
            return redirect(url_for('auth.login_page'))

    return render_template('auth/login.html')


@auth.route('/logout')
def logout_page():
    logout_user()
    flash("Logged out successfully!", category='info')
    return redirect(url_for("auth.login_page"))
