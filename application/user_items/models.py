from sqlalchemy.sql import text

from application import db


class UserItem(db.Model):
    user_item_id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('item.item_id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('account.user_id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    ordered = db.Column(db.Boolean, nullable=False)

    def __init__(self, item_id, user_id, quantity):
        self.item_id = item_id
        self.user_id = user_id
        self.quantity = quantity
        self.ordered = False

    @staticmethod
    def calc_cart_total(user_id):
        stmt = text("SELECT SUM(item.price * user_item.quantity) "
                    "FROM user_item LEFT JOIN item ON user_item.item_id = item.item_id "
                    "WHERE user_item.user_id = :user_id AND user_item.ordered = 0::boolean").params(user_id=user_id)
        result = db.engine.execute(stmt)
        return result.first()[0]
