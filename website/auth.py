from flask import redirect, request, render_template, Blueprint, flash, url_for
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from .model import Users
from . import db

auth = Blueprint('auth', __name__)


@auth.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":

        fetch_data = request.form.get

        first_name = fetch_data("firstname")
        last_name = fetch_data("lastname")
        username = fetch_data("username")
        email = fetch_data("email")
        city = fetch_data("city")
        state = fetch_data("state")
        password1 = fetch_data("password1")
        password2 = fetch_data("password2")
        propic = request.files["propic"]
        file_name = secure_filename(propic.filename)
        mime_type = propic.mimetype

        new_user = Users.query.filter_by(username=username).first()

        if new_user:
            flash("Username already taken..!", category='error')
        elif len(first_name) < 1:
            flash("First Name must be greater than 1 character", category='error')
        elif len(last_name) < 1:
            flash("Second Name must be greater than 1 character", category='error')
        elif len(username) < 1:
            flash("Username Name must be greater than 1 character", category='error')
        elif len(email) < 5:
            flash("Email must be greater than 5 characters", category='error')
        elif len(city) < 3:
            flash("City must be greater than 3 character", category='error')
        elif len(state) < 3:
            flash("State must be greater than 1 character", category='error')
        elif password1 != password2:
            flash("Passwords does not match!", category='error')
        elif len(password1) < 7:
            flash("Pawssword must be greater than 7 characters", category='error')
        else:
            new_user = Users(first_name=first_name, last_name=last_name, username=username, email=email, city=city, state=state,
                             password=generate_password_hash(password1, method='sha256'), propic=propic.read(), file_name=file_name, mime_type=mime_type)

            db.session.add(new_user)
            db.session.commit()

            login_user(new_user, remember=True)

            flash("Profile creation successful.", category='success')

            return redirect(url_for('views.home'))

    return render_template('signup.html', user=current_user)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")

        user = Users.query.filter_by(username=username).first()

        if user:
            if check_password_hash(user.password, password):
                flash("Logged in successfully...", category='success')

                login_user(user, remember=True)

                return redirect(url_for('views.home'))
            else:
                flash("Incorrect Password! Try again...", category='error')
        else:
            flash("Username does not exist! Check again...", category='error')

    return render_template('login.html', user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.home'))
