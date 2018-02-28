import json
import unittest

from tests.base import BaseTestCase
from app.data import db
from app.data.user import User


class TestAuthBlueprint(BaseTestCase):
    def test_registration(self):
        """ Test for user registration """
        with self.client:
            response = self.register_user('joe@gmail.com', '123456')
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['message'] == 'Successfully registered.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 201)

    def register_user(self, email, password):
        return self.client.post(
            '/auth/register',
            data=json.dumps(dict(
                email=email,
                password=password
            )),
            content_type='application/json'
        )

    def test_registered_with_already_registered_user(self):
        """ Test registration with already registered email"""
        user = User(
            email='joe@gmail.com',
            password='test',
            roles=[]
        )
        db.session.add(user)
        db.session.commit()
        with self.client:
            response = self.register_user('joe@gmail.com', '123456')
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'fail')
            self.assertTrue(
                data['message'] == 'User already exists. Please Log in.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 202)

    def test_registered_user_login(self):
        """ Test for login of registered-user login """
        with self.client:
            # user registration
            resp_register = self.register_user('joe@gmail.com', '123456')
            data_register = json.loads(resp_register.data.decode())
            self.assertTrue(data_register['status'] == 'success')
            self.assertTrue(
                data_register['message'] == 'Successfully registered.'
            )
            self.assertTrue(resp_register.content_type == 'application/json')
            self.assertEqual(resp_register.status_code, 201)
            # registered user login
            response = self.login_user(username='joe@gmail.com', password='123456')
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['message'] == 'Successfully logged in.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 200)

    def login_user(self, username, password):
        return self.client.post(
            '/auth/login',
            data=json.dumps(dict(
                email=username,
                password=password
            )),
            content_type='application/json'
        )

    def test_non_registered_user_login(self):
        """ Test for login of non-registered user """
        with self.client:
            response = self.login_user(username='joe@gmail.com', password='123456')
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'fail')
            self.assertTrue(data['message'] == 'User does not exist.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 404)

    def test_existed_username_and_incorrect_password_login(self):
        """ Test for login of registered-user name login but with improper password """
        with self.client:
            # user registration
            resp_register = self.register_user('joe@gmail.com', '123456')
            data_register = json.loads(resp_register.data.decode())
            self.assertTrue(data_register['status'] == 'success')
            self.assertTrue(
                data_register['message'] == 'Successfully registered.'
            )
            self.assertTrue(resp_register.content_type == 'application/json')
            self.assertEqual(resp_register.status_code, 201)
            # registered user login
            response = self.client.post(
                '/auth/login',
                data=json.dumps(dict(
                    email='joe@gmail.com',
                    password='12345'
                )),
                content_type='application/json'
            )
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'fail')
            self.assertTrue(data['message'] == 'User does not exist.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 404)

    def test_user_status(self):
        """ Test for user status """
        with self.client:
            resp_register = self.register_user('joe@gmail.com', '123456')
            response = self.client.get(
                '/auth/status')

            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['data'] is not None)
            self.assertTrue(data['data']['email'] == 'joe@gmail.com')
            self.assertEqual(response.status_code, 200)

    def test_valid_logout(self):
        """ Test for logout before token expires """
        with self.client:
            # user registration
            resp_register = self.register_user('joe@gmail.com', '123456')
            data_register = json.loads(resp_register.data.decode())
            self.assertTrue(data_register['status'] == 'success')
            self.assertTrue(
                data_register['message'] == 'Successfully registered.')
            self.assertTrue(resp_register.content_type == 'application/json')
            self.assertEqual(resp_register.status_code, 201)
            # valid token logout
            response = self.logout_user()
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['message'] == 'Successfully logged out.')
            self.assertEqual(response.status_code, 200)

    def logout_user(self):
        return self.client.post('/auth/logout')

    def test_invalid_logout(self):
        import time
        """ Testing logout after the token expires """
        with self.client:
            # user registration
            resp_register = self.register_user('joe@gmail.com', '123456')
            data_register = json.loads(resp_register.data.decode())
            self.assertTrue(data_register['status'] == 'success')
            self.assertTrue(
                data_register['message'] == 'Successfully registered.')
            self.assertTrue(resp_register.content_type == 'application/json')
            self.assertEqual(resp_register.status_code, 201)
            # waiting for session to expire
            time.sleep(6)

            # perform logout
            response = self.logout_user()
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'fail')
            self.assertTrue(
                data['message'] == 'user is not logged in')
            self.assertEqual(response.status_code, 401)

    def test_logout_of_not_logged_in_user(self):
        resp_logout = self.logout_user()
        data = json.loads(resp_logout.data.decode())
        self.assertTrue(data['status'] == 'fail')
        self.assertTrue(data['message'] == 'user is not logged in')
        self.assertEqual(resp_logout.status_code, 401)

if __name__ == '__main__':
    unittest.main()
