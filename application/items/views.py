from flask import redirect, render_template, request, url_for

from application import app, db
from application.items.models import Item


@app.route("/items/")
def items_index():
    return render_template("items/list.html", items=Item.query.all())


@app.route("/items/new/")
def items_form():
    return render_template("items/new.html")


@app.route("/items/new/", methods=["POST"])
def items_create():
    item = Item(request.form.get("name"), request.form.get("price"))
    db.session.add(item)
    db.session.commit()
    return redirect(url_for("items_index"))


@app.route("/items/change_price/<item_id>/")
def items_change_price_form(item_id):
    return render_template("items/change_price.html", item=Item.query.get(item_id))


@app.route("/items/change_price/<item_id>/", methods=["POST"])
def items_change_price(item_id):
    item = Item.query.get(item_id)
    new_price = request.form.get("new_price")
    if new_price:
        item.price = new_price
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
