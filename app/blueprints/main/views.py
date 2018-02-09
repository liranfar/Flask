import logging

from flask import Blueprint, jsonify

from app.data.author import Author
from app.data.relations import db

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return "Main"


@main.route('tasks/')
def display_tasks():
    books = {
        "Learn Python The Hard Way": {
            "author": "Shaw, Zed",
            "rating": "3.92",
            "image": "ef0ceaab-32a8-47fb-ba13-c0b362d970da.jpg"
        }
    }

    return jsonify(books)


# TODO change to POST
@main.route('users/add/<author_name>')
def add_author(author_name):
    logging.debug("got an author with name : {}".format(author_name))

    author1 = Author(author_name)  # 1
    db.session.add(author1)  # 2
    db.session.commit()

    return jsonify({'data': 'success'})
