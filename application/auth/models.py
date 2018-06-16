from application import db
from application.models import Base


class User(Base):
    __tablename__ = "account"
    username = db.Column(db.String(144), nullable=False, unique=True)
    password = db.Column(db.String(144), nullable=False)
    user_items = db.relationship("UserItem", backref='user', lazy=True)
    role = db.Column(db.String(144), nullable=False)

    def __init__(self, username, password, role):
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
