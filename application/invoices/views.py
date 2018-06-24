from flask import render_template, redirect, request, url_for
from flask_login import current_user

from application import app, db, login_manager, login_required, per_page
from application.auth.forms import UserFindForm
from application.auth.models import User
from application.invoices.models import Invoice


@app.route("/invoices")
@login_required(role="ANY")
def invoices_index():
    page = int(request.args.get("page", 1))
    if current_user.role == "ADMIN":
        invoices = Invoice.query.filter_by(payed=False).paginate(page=page, per_page=per_page)
    else:
        invoices = Invoice.query.filter_by(user_id=current_user.id, payed=False).paginate(page=page, per_page=per_page)
    return render_template("invoices/index.html", form=UserFindForm(), invoices=invoices)


@app.route("/invoices/pay/<invoice_id>")
@login_required(role="CUSTOMER")
def invoices_pay(invoice_id):
    invoice = Invoice.query.get(invoice_id)
    if invoice.user_id != current_user.id:
        return login_manager.unauthorized()
    invoice.payed = True
    db.session().commit()
    return redirect(url_for("invoices_index"))


@app.route("/invoices/reminder/<invoice_id>")
@login_required(role="ADMIN")
def invoices_reminder(invoice_id):
    invoice = Invoice.query.get(invoice_id)
    invoice.total = int(round(Invoice.interest * float(invoice.total)))
    db.session().commit()
    return redirect(url_for("invoices_index"))


@app.route("/invoices/find", methods=["POST"])
@login_required(role="ADMIN")
def invoices_find():
    form = UserFindForm(request.form)
    if not form.validate():
        invoices = Invoice.query.filter_by(payed=False).paginate(page=1, per_page=per_page)
        return render_template("invoices/index.html", form=form, invoices=invoices)
    return redirect(url_for("invoices_find_index", query=form.username.data))


@app.route("/invoices/find")
@login_required(role="ADMIN")
def invoices_find_index():
    query = request.args.get("query", "")
    page = int(request.args.get("page", 1))
    invoices = Invoice.query.filter_by(payed=False).join(Invoice.user).filter(User.username.like("%" + query + "%")) \
        .paginate(page=page, per_page=per_page)
    return render_template("invoices/index.html", form=UserFindForm(), query=query, invoices=invoices)
