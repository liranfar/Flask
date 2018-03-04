from flask import Blueprint, request, make_response, jsonify, session
from flask.views import MethodView
from flask_login import login_required

import app
from app.data.user import User

auth_blueprint = Blueprint('auth', __name__)


class RegisterAPI(MethodView):
    """
    User Registration Resource
    """

    def post(self):
        # get the post data
        post_data = request.get_json()
        # check if user already exists
        user = User.query.filter_by(email=post_data.get('email')).first()
        if not user:
            try:
                user = User(
                    email=post_data.get('email'),
                    password=post_data.get('password'),
                    roles=[]
                )

                from app import db
                # insert the user
                db.session.add(user)
                db.session.commit()

                from flask_login import login_user
                login_user(user, remember=False)

                responseObject = {
                    'status': 'success',
                    'message': 'Successfully registered.'
                }
                return make_response(jsonify(responseObject)), 201

            except Exception as e:
                responseObject = {
                    'status': 'fail',
                    'message': 'Some error occurred. Please try again.'
                }
                return make_response(jsonify(responseObject)), 401
        else:
            responseObject = {
                'status': 'fail',
                'message': 'User already exists. Please Log in.'
            }
            return make_response(jsonify(responseObject)), 202


class LoginAPI(MethodView):
    """
    User Login Resource
    """

    def post(self):
        # get the post data
        post_data = request.get_json()
        try:
            # fetch the user data
            user = User.query.filter_by(
                email=post_data.get('email')
            ).first()
            if user and app.bcrypt.check_password_hash(
                    user.password, post_data.get('password')
            ):
                from app import db
                # user.is_authenticated = True
                db.session.add(user)
                db.session.commit()

                from flask_login import login_user
                # if you change remember attribute to true it will cause
                # some issues with session duration timeout
                # see https://www.jordanbonser.com/flask-session-timeout.html
                login_user(user, remember=False)

                responseObject = {
                    'status': 'success',
                    'message': 'Successfully logged in.'
                }

                return make_response(jsonify(responseObject)), 200
            else:
                responseObject = {
                    'status': 'fail',
                    'message': 'User does not exist.'
                }
                return make_response(jsonify(responseObject)), 404
        except Exception as e:
            print(e)
            responseObject = {
                'status': 'fail',
                'message': 'Try again'
            }
            return make_response(jsonify(responseObject)), 500


class UserAPI(MethodView):
    """
    User Resource
    """

    def get(self):
        from flask_login import current_user
        if current_user:
            responseObject = {
                'status': 'success',
                'data': {
                    'user_id': current_user.id,
                    'email': current_user.email,
                    'is_authenticated': current_user.is_authenticated
                }
            }
            return make_response(jsonify(responseObject)), 200

        responseObject = {
            'status': 'fail',
            'message': 'There is no user'
        }
        return make_response(jsonify(responseObject)), 401


class LogoutAPI(MethodView):
    """
    Logout Resource
    """

    @login_required
    def post(self):

        try:
            from app import db
            # insert the token
            from flask_login import current_user
            user = current_user
            db.session.add(user)
            db.session.commit()
            from flask_login import logout_user
            logout_user()

            responseObject = {
                'status': 'success',
                'message': 'Successfully logged out.'
            }

            return make_response(jsonify(responseObject)), 200
        except Exception as e:
            responseObject = {
                'status': 'fail',
                'message': e.message
            }
            return make_response(jsonify(responseObject)), 200


# define the API resources
registration_view = RegisterAPI.as_view('register_api')
login_view = LoginAPI.as_view('login_api')
user_view = UserAPI.as_view('user_api')
logout_view = LogoutAPI.as_view('logout_api')

# add Rules for API Endpoints
auth_blueprint.add_url_rule(
    '/auth/register',
    view_func=registration_view,
    methods=['POST']
)

auth_blueprint.add_url_rule(
    '/auth/login',
    view_func=login_view,
    methods=['POST']
)

auth_blueprint.add_url_rule(
    '/auth/logout',
    view_func=logout_view,
    methods=['POST']
)

auth_blueprint.add_url_rule(
    '/auth/status',
    view_func=user_view,
    methods=['GET']
)
