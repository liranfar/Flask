"""
This file initializes your application and brings together all of the various components.
"""
import logging
import os
from flask import Flask
from flask_security import SQLAlchemyUserDatastore, Security

from app.common import config
from app.data.relations import db
from app.data.user import User
from app.data.role import Role
from app.log.log import setup_logging

from blueprints.admin.views import admin
from blueprints.main.views import main
from flask_bcrypt import Bcrypt

app = Flask(__name__,
            instance_relative_config=True)  # instance_relative_config implies loading config from instance folder


def configure_app():
    # Load the requested configuration from config module which remarked in env var
    config_name = os.getenv('FLASK_CONFIGURATION', 'default')
    app.config.from_object(config[config_name])
    # Load the configuration from the instance folder
    app.config.from_pyfile('config.py', silent=True)
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    app.security = Security(app, user_datastore)


configure_app()
setup_logging(default_level=logging.DEBUG)
logging.debug("Logger has been set up successfully")
app.register_blueprint(main, url_prefix='/')
app.register_blueprint(admin, url_prefix='/admin')
bcrypt = Bcrypt(app)
db.init_app(app)

