import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sqlalchemy.pool as pool
import psycopg2

SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database


# TODO IMPLEMENT DATABASE URL

# Base = declarative_base()
SQLALCHEMY_DATABASE_URI = 'postgresql://postgresuser:@localhost:5432/fyyur'
# engine = create_engine(SQLALCHEMY_DATABASE_URI)
# Base.metadata.create_all(engine)
#
# def getconn():
#     c = psycopg2.connect(user='postgresuser', host='localhost', dbname='test')
#     return c
#
# def conection():
#     mypool = pool.QueuePool(getconn, max_overflow=10, pool_size=5)
#     conn = mypool.connect()
#     return conn

#conxn = conection()
