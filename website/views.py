from base64 import b64encode
from flask import request, render_template, Blueprint, flash
from flask_login import login_required, current_user
from .model import Users

views = Blueprint('views', __name__)


@views.route("/")
@login_required
def home():
    user = current_user
    user_propic = b64encode(user.propic).decode('UTF-8')
    return render_template('profile.html', user_propic=user_propic, user=current_user)


@views.route('/userimg/<int:id>')
def show(id):
    obj = Users.query.filter_by(id=id).first()
    img = b64encode(obj.image).decode('UTF-8')

    return render_template('gallery.html', testing=img)
