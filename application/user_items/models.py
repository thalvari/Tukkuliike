from sqlalchemy.sql import text

from application import db
from application.models import Base


class UserItem(Base):
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    ordered = db.Column(db.Boolean, nullable=False)

    def __init__(self, item_id, user_id, quantity):
        self.item_id = item_id
        self.user_id = user_id
        self.quantity = quantity
        self.ordered = False

    def order(self):
        self.ordered = True
        self.item.stock -= self.quantity
        self.item.restock()

    @staticmethod
    def calc_cart_total(user_id):
        stmt = text("SELECT SUM(item.price * user_item.quantity) FROM user_item LEFT JOIN item "
                    "ON user_item.item_id = item.id WHERE user_item.user_id = :user_id "
                    "AND user_item.ordered = :ordered").params(user_id=user_id, ordered=False)
        result = db.engine.execute(stmt).first()[0]
        if result:
            return result
        else:
            return 0

    @staticmethod
    def calc_cart_total_in_euros(user_id):
        return "{:.2f}".format(float(UserItem.calc_cart_total(user_id)) / 100)

    @staticmethod
    def calc_ordered_count(item_id):
        stmt = text("SELECT SUM(user_item.quantity) FROM user_item LEFT JOIN item "
                    "ON user_item.item_id = item.id WHERE user_item.item_id = :item_id "
                    "AND user_item.ordered = :ordered").params(item_id=item_id, ordered=True)
        result = db.engine.execute(stmt).first()[0]
        if result:
            return result
        else:
            return 0
