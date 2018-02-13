import datetime
import logging

import jwt
from flask_security import UserMixin

# TODO from app import app causes import error ( circular dependency )
import app
from app import db
from app.data.relations import roles_users

log = logging.getLogger()


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))

    def __init__(self, email, password, active, roles):
        self.email = email
        self.password = app.bcrypt.generate_password_hash(password,
                                                          app.app.config['BCRYPT_LOG_ROUNDS'])
        self.active = active
        self.roles = roles

    def __repr__(self):
        return '<User %r>' % self.email

    def encode_auth_token(self, user_id):
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=5),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            # TODO allow access to app.config object, for now I get import error
            return jwt.encode(
                payload,
                'change_secret_key',
                algorithm='HS256'
            )
        except Exception as e:
            return e
