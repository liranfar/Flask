import unittest

from flask_testing import TestCase

from flask import current_app

from app import app


from app.common.constants import BASE_DIR

APP_INSTANCE_CONFIG_PATH = BASE_DIR + '/app/instance/config.py'


class TestDevelopmentConfig(TestCase):
    def create_app(self):
        app.config.from_object('app.config.DevelopmentConfig')
        app.config.from_pyfile(APP_INSTANCE_CONFIG_PATH, silent=True)
        return app

    def test_app_is_development(self):
        self.assertFalse(app.config['SECRET_KEY'] is 'override_me')
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertFalse(current_app is None)
        self.assertTrue(
            app.config['SQLALCHEMY_DATABASE_URI'] == 'postgresql://postgres:postgres@localhost/explore_flask'
        )


class TestTestingConfig(TestCase):
    def create_app(self):
        app.config.from_object('app.config.TestingConfig')
        app.config.from_pyfile(APP_INSTANCE_CONFIG_PATH, silent=True)
        return app

    def test_app_is_testing(self):
        self.assertFalse(app.config['SECRET_KEY'] is 'override_me')
        self.assertTrue(app.config['DEBUG'])
        self.assertTrue(
            app.config['SQLALCHEMY_DATABASE_URI'] == 'postgresql://postgres:postgres@localhost/explore_flask_test'
        )


class TestProductionConfig(TestCase):
    def create_app(self):
        app.config.from_object('app.config.ProductionConfig')
        app.config.from_pyfile(APP_INSTANCE_CONFIG_PATH, silent=True)
        return app

    def test_app_is_production(self):
        self.assertFalse(app.config['SECRET_KEY'] is 'override_me')
        self.assertTrue(app.config['DEBUG'] is False)


class TestStagingConfig(TestCase):
    def create_app(self):
        app.config.from_object('app.config.StagingConfig')
        app.config.from_pyfile(APP_INSTANCE_CONFIG_PATH, silent=True)
        return app

    def test_app_is_staging(self):
        self.assertFalse(app.config['SECRET_KEY'] is 'override_me')
        self.assertTrue(app.config['DEBUG'] is False)


if __name__ == '__main__':
    unittest.main()
