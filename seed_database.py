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

