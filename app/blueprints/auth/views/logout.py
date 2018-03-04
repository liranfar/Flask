from flask import make_response, jsonify
from flask.views import MethodView
from flask_login import login_required


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