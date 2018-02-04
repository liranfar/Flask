"""
This file initializes your application and brings together all of the various components.
"""
from flask import Flask

app = Flask(__name__, instance_relative_config=True) # instance_relative_config implies loading config from instance folder

# Load the default configuration
app.config.from_object('config.default')

# Load the configuration from the instance folder
app.config.from_pyfile('config.py')

# Load the file specified by the APP_CONFIG_FILE environment variable
# Variables defined here will override those in the default configuration
# The value of the environment variable should be the absolute path to a configuration file.
app.config.from_envvar('APP_CONFIG_FILE')