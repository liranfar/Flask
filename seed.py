from app import app, db, User, Role
from app.data.author import Author
from app.data.book import Book


def create_authors_and_books():
    author1 = Author('Ivan Vazov')
    author2 = Author('Hristo Botev')

    book1 = Book('Epic of the Forgotten', author1, '15705091.jpg', 5)
    book2 = Book('The Poems of Hristo Botev', author2, '20911420.jpg', 5)

    db.session.add(author1)
    db.session.add(author2)
    db.session.add(book1)
    db.session.add(book2)

    db.session.commit()


def create_users_and_roles():
    role = Role(name='admin')
    user = User(
        email='test@test.com',
        password='test', roles=[role]
    )
    db.session.add(user)
    db.session.add(role)

    db.session.commit()


def migrate_data():
    with app.app_context():
        db.drop_all()
        db.create_all()
        create_users_and_roles()
        create_authors_and_books()
