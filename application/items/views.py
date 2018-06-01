from flask import redirect, render_template, request, url_for

from application import app, db
from application.items.models import Item
from application.items.forms import ItemForm, ItemFindForm


@app.route("/items/")
def items_index():
    return render_template("items/list.html", form=ItemFindForm(), items=Item.query.all())


@app.route("/items/new/")
def items_new_form():
    return render_template("items/new.html", form=ItemForm())


@app.route("/items/new/", methods=["POST"])
def items_create():
    form = ItemForm(request.form)
    if not form.validate():
        return render_template("items/new.html", form=form)
    item = Item(form.name.data, form.price.data)
    db.session.add(item)
    db.session.commit()
    return redirect(url_for("items_index"))


@app.route("/items/edit/<item_id>/")
def items_edit_form(item_id):
    return render_template("items/edit.html", form=ItemForm(), item=Item.query.get(item_id))


@app.route("/items/edit/<item_id>/", methods=["POST"])
def items_edit(item_id):
    form = ItemForm(request.form)
    if not form.validate():
        return render_template("items/edit.html", form=form, item=Item.query.get(item_id))
    item = Item.query.get(item_id)
    item.name = form.name.data
    item.price = form.price.data
    db.session().commit()
    return redirect(url_for("items_index"))


@app.route("/items/delete/<item_id>/")
def items_delete(item_id):
    item = Item.query.get(item_id)
    db.session.delete(item)
    db.session().commit()
    return redirect(url_for("items_index"))


@app.route("/items/find/", methods=["POST"])
def items_find():
    form = ItemFindForm(request.form)
    return render_template("items/list.html", form=ItemFindForm(),
                           items=Item.query.filter_by(name=form.query.data).all())
