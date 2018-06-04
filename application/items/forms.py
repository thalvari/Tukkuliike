from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators
from wtforms.validators import InputRequired, Length, NumberRange

from application.items.models import Item


def item_new_validate_name(form, field):
    item = Item.query.filter_by(name=field.data).first()
    if item:
        raise validators.ValidationError("Samanniminen tuote on jo olemassa")


class ItemNewForm(FlaskForm):
    name = StringField("Nimi", [InputRequired(), Length(min=1, max=144, message="Tuotteen nimen pituus 1-144 merkkiä"),
                                item_new_validate_name])
    price = IntegerField("Hinta (sentteinä)",
                         [InputRequired(), NumberRange(min=1, max=999999, message="Syötä luku väliltä 1-999999")])

    class Meta:
        csrf = False


def item_edit_validate_name(form, field):
    item = Item.query.filter_by(name=field.data).first()
    if item:
        raise validators.ValidationError("Samanniminen tuote on jo olemassa")


class ItemEditForm(FlaskForm):
    name = StringField("Nimi", [InputRequired(), Length(min=1, max=144, message="Tuotteen nimen pituus 1-144 merkkiä"),
                                item_edit_validate_name])
    price = IntegerField("Hinta (sentteinä)",
                         [InputRequired(), NumberRange(min=1, max=999999, message="Syötä luku väliltä 1-999999")])

    class Meta:
        csrf = False


class ItemFindForm(FlaskForm):
    query = StringField("", [InputRequired(), Length(min=1, max=144, message="Tuotteen nimen pituus 1-144 merkkiä")])

    class Meta:
        csrf = False
