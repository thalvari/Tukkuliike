from application import db


class Item(db.Model):
    item_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False, unique=True)
    price = db.Column(db.Integer, nullable=False)
    date_added = db.Column(db.DateTime, default=db.func.current_timestamp())
    user_items = db.relationship("UserItem", backref='item', lazy=True)

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price_in_euros(self):
        return "{:.2f}".format(float(self.price) / 100)

    def get_date_added_no_millis(self):
        return self.date_added.strftime('%Y-%m-%d %H:%M:%S')
