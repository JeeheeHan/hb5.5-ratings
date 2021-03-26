"""Script to seed database."""
#this file imports/ties all the python files to sucessfully run DB AND server

import os
import json
from random import choice, randint
from datetime import datetime


import crud
from model import *
import server
#These next 4 lines is to call DB and then connect then create tables in DB/SQL file
os.system('dropdb ratings')
#think of this adding it directly onto the command line

#CreateDB to make the tables 
os.system('createdb ratings')


# #run dumped sql file:
# os.system('psql ratings < ratings.sql')

connect_to_db(server.app)
db.create_all()


# More code will go here

#This to open the Json movie file and read it 
with open('data/movies.json') as f:
    MOVIE_DATA = json.loads(f.read())

# Create movies, store them in list so we can use them
# to create fake ratings later
movies_in_db = []
for each_movie in MOVIE_DATA:
    # TODO: get the title, overview, and poster_path from the movie
    # dictionary. Then, get the release_date and convert it to a
    # datetime object with datetime.strptime
    title, overview, poster_path = (each_movie['title'],
                                    each_movie['overview'],
                                    each_movie['poster_path'])
    #deconstruction syntax from the MOVIE_DATA values which is a dictionary from JSON file
    release_date = datetime.datetime.strptime(each_movie['release_date'], '%Y-%m-%d')

    db_movie = crud.create_movie(title,
                                 overview,
                                 release_date,
                                 poster_path)
    #Adding the declared variables into create_movie()

    # Create a each_movie part of  here and append it to movies_in_db
    movies_in_db.append(db_movie)

