from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask import Flask
from os import path


db = SQLAlchemy()
DB_NAME = 'usersinfo'


def CreateApp():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'encrypt or secure the cookies and session data related to our website'

    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}.db'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .model import Users

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return Users.query.get(int(id))

    return app


def create_database(app):
    if not path.exists(f'website/{DB_NAME}.db'):
        db.create_all(app=app)
        print('Databse Created....!')
