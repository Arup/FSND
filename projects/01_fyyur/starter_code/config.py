import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database


# TODO IMPLEMENT DATABASE URL

Base = declarative_base()
SQLALCHEMY_DATABASE_URI = 'postgresql://postgresuser:@localhost:5432/test'
engine = create_engine(SQLALCHEMY_DATABASE_URI)
Base.metadata.create_all(engine)