from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, NumberRange


class ItemForm(FlaskForm):
    name = StringField("Nimi", [InputRequired()])
    price = IntegerField("Hinta (sentteinä)", [InputRequired(), NumberRange(min=1, message="Syötä positiivinen luku")])

    class Meta:
        csrf = False


class ItemFindForm(FlaskForm):
    query = StringField("", [InputRequired()])

    class Meta:
        csrf = False
