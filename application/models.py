from application import db


class Base(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def get_date_created_no_millis(self):
        return self.date_created.strftime('%Y-%m-%d %H:%M:%S')

    def get_date_modified_no_millis(self):
        return self.date_modified.strftime('%Y-%m-%d %H:%M:%S')
