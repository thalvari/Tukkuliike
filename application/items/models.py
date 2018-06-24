from sqlalchemy.sql import text

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

    @staticmethod
    def get_times_ordered(item_id):
        stmt = text("SELECT SUM(user_item.quantity) FROM user_item LEFT JOIN item "
                    "ON user_item.item_id = item.id WHERE user_item.item_id = :item_id "
                    "AND user_item.ordered = :ordered").params(item_id=item_id, ordered=True)
        result = db.engine.execute(stmt).first()[0]
        if result:
            return result
        else:
            return 0
