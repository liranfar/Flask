from flask import request, make_response, jsonify
from flask.views import MethodView


class LoginAPI(MethodView):
    """
    User Login Resource
    """

    def post(self):
        # get the post data
        post_data = request.get_json()
        try:
            # fetch the user data
            from app import User
            user = User.query.filter_by(
                email=post_data.get('email')
            ).first()

            from app import bcrypt
            if user and bcrypt.check_password_hash(
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
