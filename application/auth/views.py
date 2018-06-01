from flask import render_template, request, redirect, url_for
from flask_login import login_required, login_user, logout_user

from application import app, db
from application.auth.models import User
from application.auth.forms import AuthForm


@app.route("/auth/login/")
def auth_login_form():
    return render_template("auth/login.html", form=AuthForm())


@app.route("/auth/login/", methods=["POST"])
def auth_login():
    form = AuthForm(request.form)
    if form.validate():
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            form.username.errors.append("Käyttäjää ei löydy")
        elif form.password.data != user.password:
            form.password.errors.append("Salasana väärin")
        else:
            login_user(user)
            return redirect(url_for("index"))
    return render_template("auth/login.html", form=form)


@app.route("/auth/logout")
@login_required
def auth_logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/auth/register/")
def auth_register_form():
    return render_template("auth/register.html", form=AuthForm())


@app.route("/auth/register/", methods=["POST"])
def auth_register():
    form = AuthForm(request.form)
    if form.validate():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            form.username.errors.append("Käyttäjä on jo olemassa")
        else:
            user = User(form.username.data, form.password.data)
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return redirect(url_for("index"))
    return render_template("auth/register.html", form=form)
