#!/usr/bin/env bash

export FLASK_CONFIGURATION=development
export DATABASE_URL="sqlite:////home/liran/Dev/Code/Exercises/Flask/exploreFlask/db/test.db"
python seed.py
python run.py