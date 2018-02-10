import os


class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'


class ProductionConfig(BaseConfig):
    DEBUG = False


class StagingConfig(BaseConfig):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class TestingConfig(BaseConfig):
    TESTING = True
