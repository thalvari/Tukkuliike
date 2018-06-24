from flask import render_template, request, redirect, url_for
from flask_login import current_user, login_user, logout_user

from application import app, db, login_required, per_page
from application.auth.forms import UserForm, UserLoginForm, UserFindForm
from application.auth.models import User
from application.invoices.models import Invoice
from application.user_items.models import UserItem


@app.route("/auth/login")
def auth_login_form():
    return render_template("auth/login.html", form=UserLoginForm())


@app.route("/auth/login", methods=["POST"])
def auth_login():
    form = UserLoginForm(request.form)
    if not form.validate():
        return render_template("auth/login.html", form=form)
    user = User.query.filter_by(username=form.username.data).first()
    login_user(user)
    return redirect(url_for("index"))


@app.route("/auth/logout")
@login_required(role="ANY")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/auth/register")
def auth_register_form():
    return render_template("auth/register.html", form=UserForm())


@app.route("/auth/register", methods=["POST"])
def auth_register():
    form = UserForm(request.form)
    if not form.validate():
        return render_template("auth/register.html", form=form)
    user = User(form.username.data, form.password.data)
    db.session.add(user)
    db.session.commit()
    login_user(user)
    return redirect(url_for("index"))


@app.route("/auth")
@login_required(role="ADMIN")
def auth_index():
    page = int(request.args.get("page", 1))
    users = User.query.paginate(page=page, per_page=per_page)
    return render_template("auth/index.html", form=UserFindForm(), users=users)


@app.route("/auth/view/<user_id>")
@login_required(role="ADMIN")
def auth_view(user_id):
    return render_template("auth/view.html", user=User.query.get(user_id),
                           ordered_items_count=User.get_ordered_items_count(user_id))


@app.route("/auth/edit")
@login_required(role="ANY")
def auth_edit_form():
    return render_template("auth/edit.html", form=UserForm(), user=current_user)


@app.route("/auth/edit", methods=["POST"])
@login_required(role="ANY")
def auth_edit():
    form = UserForm(request.form)
    if not form.validate():
        return render_template("auth/edit.html", form=form, user=current_user)
    current_user.username = form.username.data
    current_user.password = form.password.data
    db.session().commit()
    return redirect(url_for("index"))


@app.route("/auth/delete/<user_id>")
@login_required(role="ADMIN")
def auth_delete(user_id):
    user_items = UserItem.query.filter_by(user_id=user_id).all()
    for user_item in user_items:
        db.session.delete(user_item)
    invoices = Invoice.query.filter_by(user_id=user_id).all()
    for invoice in invoices:
        db.session.delete(invoice)
    user = User.query.get(user_id)
    db.session.delete(user)
    db.session().commit()
    return redirect(url_for("auth_index"))


@app.route("/auth/find", methods=["POST"])
@login_required(role="ADMIN")
def auth_find():
    form = UserFindForm(request.form)
    if not form.validate():
        return render_template("auth/index.html", form=form, users=User.query.paginate(page=1, per_page=per_page))
    return redirect(url_for("auth_find_index", query=form.username.data))


@app.route("/auth/find")
@login_required(role="ADMIN")
def auth_find_index():
    query = request.args.get("query", "")
    page = int(request.args.get("page", 1))
    users = User.query.filter(User.username.like("%" + query + "%")).paginate(page=page, per_page=per_page)
    return render_template("auth/index.html", form=UserFindForm(), query=query, users=users)
