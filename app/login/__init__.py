from flask import make_response, jsonify
from flask_login import LoginManager


login_manager = LoginManager()
login_manager.login_view = "login"


@login_manager.user_loader
def user_loader(user_id):
    from app import User
    """Given *user_id*, return the associated User object.

    :param unicode user_id: user_id (email) user to retrieve

    """
    return User.query.get(user_id)


@login_manager.unauthorized_handler
def unauthorized_handler():
    responseObject = {
        'status': 'fail',
        'message': 'user is not logged in'
    }
    return make_response(jsonify(responseObject)), 401
