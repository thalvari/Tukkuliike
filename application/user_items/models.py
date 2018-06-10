from sqlalchemy.sql import text

from application import db


class UserItem(db.Model):
    user_item_id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('item.item_id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('account.user_id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    ordered = db.Column(db.Boolean, nullable=False)
    date_ordered = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __init__(self, item_id, user_id, quantity):
        self.item_id = item_id
        self.user_id = user_id
        self.quantity = quantity
        self.ordered = False

    def get_date_ordered_no_millis(self):
        return self.date_ordered.strftime('%Y-%m-%d %H:%M:%S')

    @staticmethod
    def calc_cart_total(user_id):
        stmt = text("SELECT SUM(item.price * user_item.quantity) FROM user_item LEFT JOIN item "
                    "ON user_item.item_id = item.item_id WHERE user_item.user_id = :user_id "
                    "AND user_item.ordered = :ordered").params(user_id=user_id, ordered=False)
        result = db.engine.execute(stmt).first()[0]
        if result:
            return "{:.2f}".format(float(result) / 100)
        else:
            return 0
