from flask import make_response, jsonify
from flask.views import MethodView


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