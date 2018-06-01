from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

from flask_sqlalchemy import SQLAlchemy

import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy(app)

from application import views
from application.auth import models, views
from application.items import models, views

from application.auth.models import User
from os import urandom

app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth_login_form"
login_manager.login_message = "Tämä toiminto vaatii kirjautumisen"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


try:
    db.create_all()
except:
    pass
