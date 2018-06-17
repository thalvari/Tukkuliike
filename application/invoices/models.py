from application import db
from application.models import Base


class Invoice(Base):
    user_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    total = db.Column(db.Integer, nullable=False)
    payed = db.Column(db.Boolean, nullable=False)

    def __init__(self, user_id, total):
        self.user_id = user_id
        self.total = total
        self.payed = False

    def get_total_in_euros(self):
        return "{:.2f}".format(float(self.total) / 100)
