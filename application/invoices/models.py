from datetime import datetime, timedelta

from application import db
from application.models import Base


class Invoice(Base):
    expiration_time = timedelta(minutes=1)
    interest = 1.1
    user_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    total = db.Column(db.Integer, nullable=False)

    def __init__(self, user_id, total):
        self.user_id = user_id
        self.total = total

    def get_total_in_euros(self):
        return "{:.2f}".format(float(self.total) / 100)

    def is_expired(self):
        return datetime.utcnow() - self.date_created > Invoice.expiration_time

    def is_reminder(self):
        return self.date_modified > self.date_created

    def get_expiration_date_no_millis(self):
        return (self.date_created + Invoice.expiration_time).strftime('%Y-%m-%d %H:%M:%S')
