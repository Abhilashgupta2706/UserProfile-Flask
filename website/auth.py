from flask import redirect, request, render_template, Blueprint, flash, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from .model import Users
from . import db

auth = Blueprint('auth', __name__)


@auth.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        propic = request.form.get("propic")
        firstname = request.form.get("firstname")
        secondname = request.form.get("secondname")
        username = request.form.get("username")
        email = request.form.get("email")
        city = request.form.get("city")
        state = request.form.get("state")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        new_user = Users.query.filter_by(username=username).first()

        if new_user:
            flash("Username already taken..!", category='error')
        elif propic:
            flash("Must select a image for profile..!", category='error')
        elif len(firstname) < 1:
            flash("First Name must be greater than 1 character", category='error')
        elif len(secondname) < 1:
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
            new_user = Users(propic=propic, firstname=firstname, secondname=secondname, username=username,
                             email=email, city=city, state=state, password=generate_password_hash(password1, method='sha256'))

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
