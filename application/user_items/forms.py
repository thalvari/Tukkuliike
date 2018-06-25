from flask_login import current_user
from wtforms import IntegerField, HiddenField
from wtforms.validators import InputRequired, NumberRange, ValidationError

from application.invoices.models import Invoice
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


def validate_invoices(form, field):
    invoices = Invoice.query.filter_by(user_id=current_user.id).all()
    for invoice in invoices:
        if invoice.is_reminder():
            raise ValidationError("Käyttäjällä on maksamattomia karhuja")


def validate_user_items(form, field):
    user_items = UserItem.query.filter_by(user_id=current_user.id, ordered=False).all()
    for user_item in user_items:
        if user_item.item.stock < user_item.quantity:
            raise ValidationError("Kaikkia tuotteita ei ole varastossa")


class UserItemOrderForm(BaseForm):
    hidden = HiddenField("", [validate_invoices, validate_user_items])
