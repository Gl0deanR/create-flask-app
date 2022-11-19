from flask import Blueprint, render_template, redirect, url_for, flash, request, abort
from flask_login import login_user, logout_user, current_user, login_required
from createflaskapp.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from createflaskapp import db
from createflaskapp.forms import EditUser, AddUser

dashboard = Blueprint('dashboard', __name__,
                      url_prefix='/',
                      template_folder='templates',
                      static_folder='static')


@dashboard.route('/')
@login_required
def home():
    """Main dashboard page."""

    return render_template('dashboard/home.html')


@dashboard.route('/users')
@login_required
def users():
    """Users page."""

    all_users = User.query.all()

    return render_template(
        'dashboard/users.html',
        all_users=all_users
    )


@dashboard.route('/users/edit/<int:user_id>', methods=['GET', 'POST'])
@login_required
def edit_user(user_id):
    """Edit user page."""

    form = EditUser()

    if request.method == 'POST':
        if form.validate_on_submit():
            user_to_update = User.query.filter_by(id=user_id).first()
            if user_to_update.username != form.username.data:
                user_to_update.username = form.username.data
            if user_to_update.first_name != form.first_name.data:
                user_to_update.first_name = form.first_name.data
            if user_to_update.last_name != form.last_name.data:
                user_to_update.last_name = form.last_name.data
            if user_to_update.email_address != form.email_address.data:
                user_to_update.email_address = form.email_address.data
            if form.password.data != '':
                user_to_update.password_hash = generate_password_hash(form.password.data, "sha256")
            db.session.commit()
            flash("User updated successfully!", category='success')
            return redirect(url_for('dashboard.edit_user', user_id=user_id))
        else:
            flash("User not updated!", category='danger')
            return redirect(url_for('dashboard.edit_user', user_id=user_id))

    user_to_edit = User.query.filter_by(id=user_id).first()

    if not user_to_edit:
        abort(404)

    return render_template(
        'dashboard/user_edit.html',
        user=user_to_edit,
        form=form
    )


@dashboard.route('/users/delete/<int:user_id>')
@login_required
def delete_user(user_id):
    """Delete user page."""

    user_to_delete = User.query.filter_by(id=user_id).first()

    if not user_to_delete:
        abort(404)

    db.session.delete(user_to_delete)
    db.session.commit()
    flash("User deleted successfully!", category='success')
    return redirect(url_for('dashboard.users'))


@dashboard.route('/users/add', methods=['GET', 'POST'])
@login_required
def add_user():
    """Add user page."""

    form = AddUser()

    if request.method == 'POST':
        if form.validate_on_submit():
            new_user = User(
                username=form.username.data,
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                email_address=form.email_address.data,
                password_hash=generate_password_hash(form.password.data, "sha256")
            )
            db.session.add(new_user)
            db.session.commit()
            flash("User added successfully!", category='success')
            return redirect(url_for('dashboard.users'))
        else:
            flash("User not added!", category='danger')
            return redirect(url_for('dashboard.add_user'))

    return render_template(
        'dashboard/user_add.html',
        form=form
    )


@dashboard.route('/register', methods=['GET', 'POST'])
def register_page():
    if request.method == 'GET':
        return render_template('dashboard/register.html')

    if request.method == 'POST':
        if request.form.get('username') == "" or request.form.get('email_address') == "" or request.form.get(
                'last_name') == "" or request.form.get('first_name') == "" or request.form.get('password') == "":
            flash("All fields must be filled in!", category='success')
            return redirect(url_for('dashboard.register_page'))

        user = User.query.filter_by(email_address=request.form.get('email_address')).first()
        if user is None:
            # Hash the password
            hashed_pw = generate_password_hash(request.form.get('password'), "sha256")
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
            return redirect(url_for('dashboard.login_page'))

        else:
            flash("User already exists!", category='success')
            return redirect(url_for('dashboard.login_page'))

    return render_template('dashboard/register.html')


@dashboard.route('/login', methods=['GET', 'POST'])
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
                return redirect(url_for('dashboard.login_page'))
        else:
            flash('User does not exist.', category='danger')
            return redirect(url_for('dashboard.login_page'))

    return render_template('dashboard/login.html')


@dashboard.route('/logout')
def logout_page():
    logout_user()
    flash("Logged out successfully!", category='info')
    return redirect(url_for("dashboard.login_page"))


@dashboard.app_errorhandler(404)
def page_not_found_404(e):
    return render_template("dashboard/404.html"), 404


@dashboard.app_errorhandler(500)
def page_not_found_500(e):
    return render_template("dashboard/500.html"), 500
