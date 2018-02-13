import os

basedir = os.path.abspath(os.path.dirname(__file__))
POSTGRES_BASE = os.getenv('POSTGRES_BASE')
DATABASE_NAME = os.getenv('DATABASE_NAME', 'explore_flask')


class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CSRF_ENABLED = True
    BCRYPT_LOG_ROUNDS = 13
    SQLALCHEMY_DATABASE_URI = POSTGRES_BASE + DATABASE_NAME


class ProductionConfig(BaseConfig):
    DEBUG = False
    SECRET_KEY = 'OVERRIDE_ME'


class StagingConfig(BaseConfig):
    DEVELOPMENT = True
    DEBUG = False
    SECRET_KEY = 'OVERRIDE_ME'


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 4
    SECRET_KEY = 'OVERRIDE_ME'


class TestingConfig(BaseConfig):
    TESTING = True
    DEBUG = True
    SECRET_KEY = 'OVERRIDE_ME'
    BCRYPT_LOG_ROUNDS = 4
    PRESERVE_CONTEXT_ON_EXCEPTION = False
