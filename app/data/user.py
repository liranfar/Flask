from flask_login import UserMixin
from app.data import db
from app.data.relations import roles_users

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))

    def __init__(self, email, password, roles):
        self.email = email
        self.roles = roles
        from app import bcrypt, app
        self.password = bcrypt.generate_password_hash(password,
                                                      app.config['BCRYPT_LOG_ROUNDS'])

    def __repr__(self):
        return '<User %r>' % self.email

