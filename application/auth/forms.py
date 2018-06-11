from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
from wtforms.validators import InputRequired, Length, ValidationError

from application.auth.models import User


def user_validate_username(form, field):
    user = User.query.filter_by(username=field.data).first()
    if user and (not current_user.is_authenticated or user.id != current_user.id):
        raise ValidationError("Käyttäjä on jo olemassa")


class UserForm(FlaskForm):
    username = StringField("Käyttäjänimi",
                           [InputRequired(), Length(min=4, max=144, message="Käyttäjänimen pituus 4-144 merkkiä"),
                            user_validate_username])
    password = PasswordField("Salasana",
                             [InputRequired(), Length(min=8, max=144, message="Salasanan pituus 8-144 merkkiä")])

    class Meta:
        csrf = False


def user_login_validate_username(form, field):
    user = User.query.filter_by(username=field.data).first()
    if not user:
        raise ValidationError("Käyttäjää ei löydy")


def user_login_validate_password(form, field):
    user = User.query.filter_by(username=form.username.data).first()
    if user and field.data != user.password:
        raise ValidationError("Salasana väärin")


class UserLoginForm(UserForm):
    username = StringField("Käyttäjänimi",
                           [InputRequired(), Length(min=4, max=144, message="Käyttäjänimen pituus 4-144 merkkiä"),
                            user_login_validate_username])
    password = PasswordField("Salasana",
                             [InputRequired(), Length(min=8, max=144, message="Salasanan pituus 8-144 merkkiä"),
                              user_login_validate_password])
