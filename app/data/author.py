from app import db


class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)
    names = db.Column(db.String(100), unique=True)

    def __init__(self, names):
        self.names = names

    def __repr__(self):
        return '<Author %r>' % self.names
