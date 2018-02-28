from flask_login import UserMixin, LoginManager
# from flask_security import UserMixin

# TODO from app import app causes import error ( circular dependency )
import app
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
        # TODO: remove bcrypt from app for disabling 'import app'
        self.password = app.bcrypt.generate_password_hash(password,
                                                          app.app.config['BCRYPT_LOG_ROUNDS'])
        self.roles = roles

    def __repr__(self):
        return '<User %r>' % self.email


# Login Manager
login_manager = LoginManager()
login_manager.login_view = "login"


@login_manager.user_loader
def user_loader(user_id):
    """Given *user_id*, return the associated User object.

    :param unicode user_id: user_id (email) user to retrieve

    """
    return User.query.get(user_id)

