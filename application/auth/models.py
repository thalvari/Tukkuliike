from application import db


class User(db.Model):
    __tablename__ = "account"
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(144), nullable=False, unique=True)
    password = db.Column(db.String(144), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def get_id(self):
        return self.user_id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True
