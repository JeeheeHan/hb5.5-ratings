"""CRUD operations."""

from model import *


def create_user(eml, pwd):
    """Create and return a new user."""

    user = User(email=eml, password=pwd)

    db.session.add(user)
    db.session.commit()

    return user


def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie."""

    movie = Movie(title=title,
                  overview=overview,
                  release_date=release_date,
                  poster_path=poster_path)

    db.session.add(movie)
    db.session.commit()

    return movie

def get_movies():
    """Return all movies."""

    return Movie.query.all()

def get_movie_by_id(movie_id):
    """Return movies by ID"""

    return Movie.query.get(movie_id)    

def create_rating(user, movie, score):
    """Create and return a new rating."""

    rating = Rating(user=user, movie=movie, score=score)

    db.session.add(rating)
    db.session.commit()

    return rating

# def get_users():
#     """Return all users."""

#     return User.query.all()

def get_user_by_email(email):
    """Return a user by email"""
    
    return User.query.filter(User.email == email).first()
    #Return the first result of this Query or None if the result doesn’t contain any row.

def login_check(email, password):
    """Check if email matches password"""
    try: 
        user = User.query.filter(User.email == email).first()
        password_by_email = user.password

        if password == password_by_email:
            return user.user_id
    except:
        pass

if __name__ == '__main__':
    from server import app
    connect_to_db(app)