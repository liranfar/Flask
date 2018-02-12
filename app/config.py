import os

basedir = os.path.abspath(os.path.dirname(__file__))
POSTGRES_LOCAL_BASE = 'postgresql://postgres:postgres@localhost/'
DATABASE_NAME = 'explore_flask'


class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CSRF_ENABLED = True
    SECRET_KEY = os.getenv('SECRET_KEY', 'override_me')
    BCRYPT_LOG_ROUNDS = 13


class ProductionConfig(BaseConfig):
    DEBUG = False
    SECRET_KEY = 'my_precious'
    SQLALCHEMY_DATABASE_URI = 'postgresql:///todo'

class StagingConfig(BaseConfig):
    DEVELOPMENT = True
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql:///todo'
    SECRET_KEY = 'my_precious'

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = POSTGRES_LOCAL_BASE + DATABASE_NAME
    BCRYPT_LOG_ROUNDS = 4


class TestingConfig(BaseConfig):
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = POSTGRES_LOCAL_BASE + DATABASE_NAME + '_test'
    BCRYPT_LOG_ROUNDS = 4
    PRESERVE_CONTEXT_ON_EXCEPTION = False
