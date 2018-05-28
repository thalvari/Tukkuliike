from flask import redirect, render_template, request, url_for

from application import app, db
from application.items.models import Item


@app.route("/items/")
def items_index():
    return render_template("items/list.html", items=Item.query.all())


@app.route("/items/new/")
def items_new_form():
    return render_template("items/new.html")


@app.route("/items/new/", methods=["POST"])
def items_create():
    name = request.form.get("name")
    price = request.form.get("price")
    if name and price and int(price) > 0:
        item = Item(name, price)
        db.session.add(item)
        db.session.commit()
    return redirect(url_for("items_index"))


@app.route("/items/edit/<item_id>/")
def items_edit_form(item_id):
    return render_template("items/edit.html", item=Item.query.get(item_id))


@app.route("/items/edit/<item_id>/", methods=["POST"])
def items_edit(item_id):
    item = Item.query.get(item_id)
    name = request.form.get("name")
    price = request.form.get("price")
    if name:
        item.name = name
    if price and int(price) > 0:
        item.price = price
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
    query = request.form.get("query")
    return render_template("items/list.html", items=Item.query.filter_by(name=query).all())
