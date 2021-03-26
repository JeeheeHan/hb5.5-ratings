"""CRUD operations."""

from model import *


def create_user(eml, pwd):
    """Create and return a new user."""

    user = User(email=eml, password=pwd)

    db.session.add(user)
    db.session.commit()

    return user










if __name__ == '__main__':
    from server import app
    connect_to_db(app)