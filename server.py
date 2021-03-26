"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session, redirect)

from model import connect_to_db
import crud
from jinja2 import StrictUndefined 

app = Flask(__name__)
app.secret_key = "dev"

#to throw errors at us for undefined variables
app.jinja_env.undefined = StrictUndefined

# Replace this with routes and view functions!
@app.route ('/')
def homepage ():
    """Go to homepage"""
    
    return render_template('homepage.html')

@app.route ('/movies')
def all_movies():
    """Gets all movies"""

    movies = crud.get_movies()
    return render_template('all_movies.html', movies=movies)


@app.route ('/movies/<movie_id>')
def show_movie(movie_id):
    """Show details on a particular movie."""

    movie = crud.get_movie_by_id(movie_id)
    return render_template('movie_details.html', movie=movie)


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
