from flask import request, make_response, jsonify
from flask.views import MethodView


class RegisterAPI(MethodView):
    """
    User Registration Resource
    """

    def post(self):
        # get the post data
        post_data = request.get_json()
        # check if user already exists

        from app import User
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
