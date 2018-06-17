from flask_login import current_user
from wtforms import IntegerField
from wtforms.validators import InputRequired, NumberRange, ValidationError

from application.models import BaseForm
from application.user_items.models import UserItem


class UserItemForm(BaseForm):
    quantity = IntegerField("Määrä", [InputRequired(), NumberRange(min=1, max=99, message="Syötä luku väliltä 1-99")])


def validate_item_id(form, field):
    if UserItem.query.filter_by(item_id=form.item_id, user_id=current_user.id, ordered=False).first():
        raise ValidationError("Tuote on jo ostoskorissa")


class UserItemCheckForm(BaseForm):
    item_id = 0
    quantity = IntegerField("Määrä", [InputRequired(), NumberRange(min=1, max=99, message="Syötä luku väliltä 1-99"),
                                      validate_item_id])
