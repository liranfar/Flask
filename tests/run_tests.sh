#!/usr/bin/env bash

export FLASK_CONFIGURATION='test'
export DATABASE_NAME='explore_flask_test'
export POSTGRES_BASE='postgresql://postgres:postgres@localhost/'
python manage.py test