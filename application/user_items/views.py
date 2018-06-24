from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application import app, db, login_manager, login_required, per_page
from application.invoices.models import Invoice
from application.items.models import Item
from application.user_items.forms import UserItemForm, UserItemCheckForm, UserItemOrderForm
from application.user_items.models import UserItem


@app.route("/user_items/cart")
@login_required(role="CUSTOMER")
def user_items_cart_index():
    page = int(request.args.get("page", 1))
    user_items = UserItem.query.filter_by(user_id=current_user.id, ordered=False).paginate(page=page, per_page=per_page)
    return render_template("user_items/cart.html", form=UserItemOrderForm(),
                           cart_total=UserItem.calc_cart_total_in_euros(current_user.id), user_items=user_items)


@app.route("/user_items/ordered")
@login_required(role="CUSTOMER")
def user_items_ordered_index():
    page = int(request.args.get("page", 1))
    user_items = UserItem.query.filter_by(user_id=current_user.id, ordered=True).paginate(page=page, per_page=per_page)
    return render_template("user_items/ordered.html", user_items=user_items)


@app.route("/user_items/new/<item_id>", methods=["POST"])
@login_required(role="CUSTOMER")
def user_items_create(item_id):
    form = UserItemCheckForm(request.form)
    form.item_id = int(item_id)
    if not form.validate():
        return render_template("items/view.html", form=form, item=Item.query.get(item_id))
    user_item = UserItem(item_id, current_user.id, form.quantity.data)
    db.session.add(user_item)
    db.session.commit()
    return redirect(url_for("user_items_cart_index"))


@app.route("/user_items/edit/<user_item_id>")
@login_required(role="CUSTOMER")
def user_items_edit_form(user_item_id):
    user_item = UserItem.query.get(user_item_id)
    if user_item.user_id != current_user.id:
        return login_manager.unauthorized()
    return render_template("user_items/edit.html", form=UserItemForm(), user_item=user_item)


@app.route("/user_items/edit/<user_item_id>", methods=["POST"])
@login_required(role="CUSTOMER")
def user_items_edit(user_item_id):
    form = UserItemForm(request.form)
    user_item = UserItem.query.get(user_item_id)
    if not form.validate():
        return render_template("user_items/edit.html", form=form, user_item=user_item)
    user_item.quantity = form.quantity.data
    db.session().commit()
    return redirect(url_for("user_items_cart_index"))


@app.route("/user_items/delete/<user_item_id>")
@login_required(role="CUSTOMER")
def user_items_delete(user_item_id):
    user_item = UserItem.query.get(user_item_id)
    db.session.delete(user_item)
    db.session().commit()
    return redirect(url_for("user_items_cart_index"))


@app.route("/user_items/order", methods=["POST"])
@login_required(role="CUSTOMER")
def user_items_order():
    form = UserItemOrderForm(request.form)
    if not form.validate():
        user_items = UserItem.query.filter_by(user_id=current_user.id, ordered=False) \
            .paginate(page=1, per_page=per_page)
        return render_template("user_items/cart.html", form=form,
                               cart_total=UserItem.calc_cart_total_in_euros(current_user.id), user_items=user_items)
    invoice = Invoice(current_user.id, UserItem.calc_cart_total(current_user.id))
    db.session.add(invoice)
    user_items = UserItem.query.filter_by(user_id=current_user.id, ordered=False).all()
    for user_item in user_items:
        user_item.order()
    db.session().commit()
    return redirect(url_for("user_items_ordered_index"))
