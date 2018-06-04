from flask import render_template, request, redirect, url_for
from flask_login import current_user, login_required, login_user, logout_user

from application import app, db
from application.auth.models import User
from application.auth.forms import UserForm, UserLoginForm


@app.route("/auth/login/")
def auth_login_form():
    return render_template("auth/login.html", form=UserLoginForm())


@app.route("/auth/login/", methods=["POST"])
def auth_login():
    form = UserLoginForm(request.form)
    if not form.validate():
        return render_template("auth/login.html", form=form)
    user = User.query.filter_by(username=form.username.data).first()
    login_user(user)
    return redirect(url_for("index"))


@app.route("/auth/logout")
@login_required
def auth_logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/auth/register/")
def auth_register_form():
    return render_template("auth/register.html", form=UserForm())


@app.route("/auth/register/", methods=["POST"])
def auth_register():
    form = UserForm(request.form)
    if not form.validate():
        return render_template("auth/register.html", form=form)
    user = User(form.username.data, form.password.data)
    db.session.add(user)
    db.session.commit()
    login_user(user)
    return redirect(url_for("index"))


@app.route("/auth/")
@login_required
def auth_index():
    return render_template("auth/index.html", users=User.query.all())


@app.route("/auth/edit/")
@login_required
def auth_edit_form():
    return render_template("auth/edit.html", form=UserForm(), user=current_user)


@app.route("/users/edit/", methods=["POST"])
@login_required
def auth_edit():
    form = UserForm(request.form)
    if form.username.data != current_user.username and not form.validate():
        return render_template("auth/edit.html", form=form, user=current_user)
    current_user.username = form.username.data
    current_user.password = form.password.data
    db.session().commit()
    return redirect(url_for("index"))
