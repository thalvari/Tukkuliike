from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, Length, NumberRange, ValidationError

from application.items.models import Item


def item_validate_name(form, field):
    item = Item.query.filter_by(name=field.data).first()
    if item and item.item_id != form.item_id:
        raise ValidationError("Samanniminen tuote on jo olemassa")


class ItemForm(FlaskForm):
    item_id = 0
    name = StringField("Nimi", [InputRequired(), Length(min=1, max=144, message="Nimen pituus 1-144 merkkiä"),
                                item_validate_name])
    price = IntegerField("Hinta (sentteinä)",
                         [InputRequired(), NumberRange(min=1, max=999999, message="Syötä luku väliltä 1-999999")])

    class Meta:
        csrf = False


class ItemFindForm(FlaskForm):
    name = StringField("", [InputRequired(), Length(min=1, max=144, message="Nimen pituus 1-144 merkkiä")])

    class Meta:
        csrf = False
