#!/usr/bin/env bash

export FLASK_CONFIGURATION='development'
export DATABASE_NAME='explore_flask'
export POSTGRES_BASE='postgresql://postgres:postgres@localhost/'
# python manage.py db init
# python manage.py db migrate
python manage.py db upgrade
# python manage.py db downgrade
# python manage.py runserver
# python manage.py seed
# python seed.py
# python run.py