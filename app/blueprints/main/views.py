import logging

from flask import Blueprint, jsonify, render_template

from app.data.author import Author
from app.data.relations import db

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('todo-data.json')
def display_tasks():
    tasks = [
        {
            "id": 0,
            "text": "Make API calls simpler",
            "completed": False
        },
        {
            "id": 1,
            "text": "Profit",
            "completed": False
        }
    ]

    return jsonify(tasks)


@main.route('authors/add/<author_name>', methods=['POST'])
def add_author(author_name):
    logging.debug("got an author with name : {}".format(author_name))

    author1 = Author(author_name)  # 1
    db.session.add(author1)  # 2
    db.session.commit()

    return jsonify({'data': 'success'})


@main.route('hello')
def hello():
    # return jsonify({'data': 'success'})
    return render_template('hello.html')
