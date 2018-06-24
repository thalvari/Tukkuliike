from sqlalchemy import text

from application import db
from application.models import Base


class User(Base):
    __tablename__ = "account"
    username = db.Column(db.String(144), nullable=False, unique=True)
    password = db.Column(db.String(144), nullable=False)
    role = db.Column(db.String(144), nullable=False)
    user_items = db.relationship("UserItem", backref='user', lazy=True)
    invoices = db.relationship("Invoice", backref='user', lazy=True)

    def __init__(self, username, password, role="CUSTOMER"):
        self.username = username
        self.password = password
        self.role = role

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    @staticmethod
    def get_ordered_items_count(user_id):
        stmt = text("SELECT SUM(user_item.quantity) FROM user_item LEFT JOIN account "
                    "ON user_item.user_id = account.id WHERE user_item.user_id = :user_id "
                    "AND user_item.ordered = :ordered").params(user_id=user_id, ordered=True)
        result = db.engine.execute(stmt).first()[0]
        if result:
            return result
        else:
            return 0
