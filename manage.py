import unittest

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import app, db
# TODO: do not remove these imports, otherwise alembic will not detect all tables
# from app.data.author import Author
# from app.data.book import Book
from app.data.blacklist import BlacklistToken
from seed import migrate_data

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


# TODO EXPLORE-FLASK-1: Move seed/data migration into the migration script
@manager.command
def seed():
    migrate_data()


@manager.command
def test():
    """Runs the unit tests without test coverage."""
    tests = unittest.TestLoader().discover('tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    manager.run()
