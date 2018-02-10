from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import app, db
# TODO: do not remove these imports, otherwise alembic will not detect all tables
from app.data.author import Author
from app.data.book import Book


migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

# TODO EXPLORE-FLASK-1: Move seed/data migration into the migration script
# @manager.command
# def seed():
#     import seed


if __name__ == '__main__':
    manager.run()
