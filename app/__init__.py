"""
This file initializes your application and brings together all of the various components.
"""
import os
from flask import Flask

from app.common import config
from blueprints.admin.views import admin
from blueprints.main.views import main

app = Flask(__name__,
            instance_relative_config=True)  # instance_relative_config implies loading config from instance folder


def configure_app():
    # Load the requested configuration from config module which remarked in env var
    config_name = os.getenv('FLASK_CONFIGURATION', 'default')
    app.config.from_object(config[config_name])
    # Load the configuration from the instance folder
    app.config.from_pyfile('config.py', silent=True)

configure_app()

app.register_blueprint(main, url_prefix='/')
app.register_blueprint(admin, url_prefix='/admin')
