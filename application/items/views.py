from flask import redirect, render_template, request, url_for

from application import app, db, login_required, per_page
from application.items.forms import ItemForm, ItemFindForm
from application.items.models import Item
from application.user_items.forms import UserItemCheckForm
from application.user_items.models import UserItem


@app.route("/items")
def items_index():
    page = int(request.args.get("page", 1))
    items = Item.query.paginate(page=page, per_page=per_page)
    return render_template("items/index.html", form=ItemFindForm(), items=items)


@app.route("/items/new")
@login_required(role="ADMIN")
def items_new_form():
    return render_template("items/new.html", form=ItemForm())


@app.route("/items/new", methods=["POST"])
@login_required(role="ADMIN")
def items_create():
    form = ItemForm(request.form)
    if not form.validate():
        return render_template("items/new.html", form=form)
    item = Item(form.name.data, form.price.data, form.threshold.data)
    db.session.add(item)
    db.session.commit()
    return redirect(url_for("items_index"))


@app.route("/items/view/<item_id>")
def items_view(item_id):
    return render_template("items/view.html", form=UserItemCheckForm(), item=Item.query.get(item_id),
                           times_ordered=Item.get_times_ordered(item_id))


@app.route("/items/edit/<item_id>")
@login_required(role="ADMIN")
def items_edit_form(item_id):
    return render_template("items/edit.html", form=ItemForm(), item=Item.query.get(item_id))


@app.route("/items/edit/<item_id>", methods=["POST"])
@login_required(role="ADMIN")
def items_edit(item_id):
    form = ItemForm(request.form)
    item = Item.query.get(item_id)
    form.item_id = item.id
    if not form.validate():
        return render_template("items/edit.html", form=form, item=item)
    item.name = form.name.data
    item.price = form.price.data
    item.threshold = form.threshold.data
    db.session().commit()
    return redirect(url_for("items_index"))


@app.route("/items/delete/<item_id>")
@login_required(role="ADMIN")
def items_delete(item_id):
    user_items = UserItem.query.filter_by(item_id=item_id).all()
    for user_item in user_items:
        db.session.delete(user_item)
    item = Item.query.get(item_id)
    db.session.delete(item)
    db.session().commit()
    return redirect(url_for("items_index"))


@app.route("/items/find", methods=["POST"])
def items_find():
    form = ItemFindForm(request.form)
    if not form.validate():
        return render_template("items/index.html", form=form, items=Item.query.paginate(page=1, per_page=per_page))
    return redirect(url_for("items_find_index", query=form.name.data))


@app.route("/items/find")
def items_find_index():
    query = request.args.get("query", "")
    page = int(request.args.get("page", 1))
    items = Item.query.filter(Item.name.like("%" + query + "%")).paginate(page=page, per_page=per_page)
    return render_template("items/index.html", form=ItemFindForm(), query=query, items=items)
