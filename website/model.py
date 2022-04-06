from . import db
from flask_login import UserMixin
from sqlalchemy import func


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    propic = db.Column(db.Text, nullable=False)
    firstname = db.Column(db.String(30), nullable=False)
    secondname = db.Column(db.String(30), nullable=False)
    username = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(50),  nullable=False)
    city = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(30), nullable=False)
