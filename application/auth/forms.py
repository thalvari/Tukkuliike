from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
from wtforms.validators import InputRequired, Length


class AuthForm(FlaskForm):
    username = StringField("Käyttäjänimi", [InputRequired()])
    password = PasswordField("Salasana",
                             [InputRequired(), Length(min=8, message="Salasanan oltava vähintään 8 merkkiä pitkä")])

    class Meta:
        csrf = False
