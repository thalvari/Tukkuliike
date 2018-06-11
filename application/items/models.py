from application import db
from application.models import Base


class Item(Base):
    name = db.Column(db.String(144), nullable=False, unique=True)
    price = db.Column(db.Integer, nullable=False)
    user_items = db.relationship("UserItem", backref='item', lazy=True)

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price_in_euros(self):
        return "{:.2f}".format(float(self.price) / 100)
