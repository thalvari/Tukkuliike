from flask import render_template, redirect, url_for
from flask_login import current_user

from application import app, db, login_manager, login_required
from application.invoices.models import Invoice


@app.route("/invoices")
@login_required(role="ANY")
def invoices_index():
    if current_user.role == "ADMIN":
        return render_template("invoices/index.html", invoices=Invoice.query.filter_by(payed=False).all())
    else:
        return render_template("invoices/index.html",
                               invoices=Invoice.query.filter_by(user_id=current_user.id, payed=False).all())


@app.route("/invoices/pay/<invoice_id>")
@login_required(role="CUSTOMER")
def invoices_pay(invoice_id):
    invoice = Invoice.query.get(invoice_id)
    if invoice.user_id != current_user.id:
        return login_manager.unauthorized()
    invoice.payed = True
    db.session().commit()
    return redirect(url_for("invoices_index"))
