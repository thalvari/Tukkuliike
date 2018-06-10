from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.items.models import Item
from application.user_items.forms import UserItemForm, UserItemCheckForm
from application.user_items.models import UserItem


@app.route("/user_items/cart")
@login_required
def user_items_cart_index():
    return render_template("user_items/cart.html", cart_total=UserItem.calc_cart_total(current_user.user_id),
                           user_items=UserItem.query.filter_by(user_id=current_user.user_id, ordered=False).all())


@app.route("/user_items/ordered")
@login_required
def user_items_ordered_index():
    return render_template("user_items/ordered.html",
                           user_items=UserItem.query.filter_by(user_id=current_user.user_id, ordered=True).all())


@app.route("/user_items/new/<item_id>", methods=["POST"])
@login_required
def user_items_create(item_id):
    form = UserItemCheckForm(request.form)
    form.item_id = int(item_id)
    if not form.validate():
        return render_template("items/view.html", form=form, item=Item.query.get(item_id))
    user_item = UserItem(item_id, current_user.user_id, form.quantity.data)
    db.session.add(user_item)
    db.session.commit()
    return redirect(url_for("user_items_cart_index"))


@app.route("/user_items/edit/<user_item_id>")
@login_required
def user_items_edit_form(user_item_id):
    return render_template("user_items/edit.html", form=UserItemForm(), user_item=UserItem.query.get(user_item_id))


@app.route("/user_items/edit/<user_item_id>", methods=["POST"])
@login_required
def user_items_edit(user_item_id):
    form = UserItemForm(request.form)
    user_item = UserItem.query.get(user_item_id)
    if not form.validate():
        return render_template("user_items/edit.html", form=form, user_item=user_item)
    user_item.quantity = form.quantity.data
    db.session().commit()
    return redirect(url_for("user_items_cart_index"))


@app.route("/user_items/delete/<user_item_id>")
@login_required
def user_items_delete(user_item_id):
    user_item = UserItem.query.get(user_item_id)
    db.session.delete(user_item)
    db.session().commit()
    return redirect(url_for("user_items_cart_index"))


@app.route("/user_items/order", methods=["POST"])
@login_required
def user_items_order():
    user_items = UserItem.query.filter_by(user_id=current_user.user_id, ordered=False).all()
    for user_item in user_items:
        user_item.ordered = True
        user_item.date_ordered = db.func.current_timestamp()
    db.session().commit()
    return redirect(url_for("user_items_ordered_index"))
