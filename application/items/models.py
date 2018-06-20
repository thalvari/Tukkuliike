from application import db
from application.models import Base


class Item(Base):
    name = db.Column(db.String(144), nullable=False, unique=True)
    price = db.Column(db.Integer, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    threshold = db.Column(db.Integer, nullable=False)
    user_items = db.relationship("UserItem", backref='item', lazy=True)

    def __init__(self, name, price, threshold):
        self.name = name
        self.price = price
        self.threshold = threshold
        self.stock = 2 * threshold

    def get_price_in_euros(self):
        return "{:.2f}".format(float(self.price) / 100)

    def restock(self):
        if self.stock < self.threshold:
            self.stock += 2 * self.threshold
