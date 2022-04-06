import imp
from flask import request, render_template, Blueprint, flash
from flask_login import login_required, current_user
from .model import Users

views = Blueprint('views', __name__)


@views.route("/")
@login_required
def home():
    return render_template('profile.html', user=current_user)
