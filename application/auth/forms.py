from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
from wtforms.validators import InputRequired, Length

from application.auth.models import User


def user_validate_username(form, field):
    user = User.query.filter_by(username=field.data).first()
    if user:
        raise validators.ValidationError("Käyttäjä on jo olemassa")


class UserForm(FlaskForm):
    username = StringField("Käyttäjänimi",
                           [InputRequired(),
                            Length(min=4, max=144, message="Käyttäjänimen pituus 4-144 merkkiä"),
                            user_validate_username])
    password = PasswordField("Salasana",
                             [InputRequired(),
                              Length(min=8, max=144, message="Salasanan pituus 8-144 merkkiä")])

    class Meta:
        csrf = False


def login_validate_username(form, field):
    user = User.query.filter_by(username=field.data).first()
    if not user:
        raise validators.ValidationError("Käyttäjää ei löydy")


def login_validate_password(form, field):
    user = User.query.filter_by(username=form.username.data).first()
    if user and field.data != user.password:
        raise validators.ValidationError("Salasana väärin")


class UserLoginForm(UserForm):
    username = StringField("Käyttäjänimi",
                           [InputRequired(),
                            Length(min=4, max=144, message="Käyttäjänimen pituus 4-144 merkkiä"),
                            login_validate_username])
    password = PasswordField("Salasana",
                             [InputRequired(),
                              Length(min=8, max=144, message="Salasanan pituus 8-144 merkkiä"),
                              login_validate_password])
