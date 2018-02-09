class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:////home/liran/Dev/Code/Exercises/Flask/exploreFlask/db/test.db'


class TestingConfig(BaseConfig):
    DEBUG = False
    TESTING = True
