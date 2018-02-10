#!/usr/bin/env bash

export FLASK_CONFIGURATION='development'
export DATABASE_URL='postgresql://postgres:postgres@localhost/explore_flask'
# export DATABASE_URL="sqlite:////home/liran/Dev/Code/Exercises/Flask/exploreFlask/db/test.db"
# python manage.py db init
# python manage.py db migrate
# python manage.py db upgrade
# python manage.py db downgrade
python manage.py runserver
# python manage.py seed
# python seed.py
# python run.py