import os
from functools import wraps
from os import urandom

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager, current_user
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
Bootstrap(app)
if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy(app)
app.config["SECRET_KEY"] = urandom(32)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth_login_form"
login_manager.login_message = "Tämä toiminto vaatii kirjautumisen"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


def login_required(role="ANY"):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if current_user.is_authenticated and (role == "ANY" or role == current_user.role):
                return fn(*args, **kwargs)
            else:
                return login_manager.unauthorized()

        return decorated_view

    return wrapper


from application import models, views
from application.auth import models, views
from application.items import models, views
from application.user_items import models, views
from application.auth.models import User

try:
    db.create_all()
    user = User("admin", "password", "ADMIN")
    db.session.add(user)
    db.session.commit()
except:
    pass
