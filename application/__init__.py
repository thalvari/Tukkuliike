from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

from flask_sqlalchemy import SQLAlchemy

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///items.db"
app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy(app)

from application import views
from application.items import models, views

db.create_all()
