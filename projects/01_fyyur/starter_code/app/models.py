from . import db
import os
import json
import logging
from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Boolean, PickleType

class DataValidationError(ValueError):
    pass

class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(Integer, primary_key=True)
    name = db.Column(String)
    city = db.Column(String(120))
    state = db.Column(String(120))
    address = db.Column(String(120))
    phone = db.Column(String(120))
    image_link = db.Column(String(500))
    facebook_link = db.Column(String(120))

    def __repr__(self):
       return "<Artist(name='%s', city='%s', state='%s', phone='%s', genres='%s', image_link='%s' facebook_link='%s')>" % \
              (self.name, self.city, self.state, self.phone, self.genres, self.image_link, self.facebook_link)
    # TODO: implement any missing fields, as a database migration using Flask-Migrate

    def save(self):
        """ Saves an existing Category in the database """
        # if the id is None it hasn't been added to the database
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        """ Deletes a Category from the database """
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def init_db(cls):
        """ Initializes the database session """
        cls.logger.info('Venue: Initializing database')
        db.create_all()  # make our sqlalchemy tables

    @classmethod
    def delete_all(cls):
        cls.query.delete()
        db.session.commit()

    @classmethod
    def all(cls):
        """ Return all of the Categories in the database """
        cls.logger.info('Processing all Venues')
        return cls.query.all()

    @classmethod
    def find(cls, id):
        """ Find a Category by it's id """
        cls.logger.info('Processing Venue lookup for id %s ...', id)
        return cls.query.get(id)

    @classmethod
    def find_or_404(cls, id):
        """ Find a Category by it's id """
        cls.logger.info('Processing Venue lookup or 404 for id %s ...', id)
        return cls.query.get_or_404(id)

    @classmethod
    def find_by_name(cls, name):
        """ Query that finds Categories by their name """
        cls.logger.info('Processing Venue name query for %s ...', name)
        return cls.query.filter(Venue.name == name)

class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(Integer, primary_key=True)
    name = db.Column(String)
    city = db.Column(String(120))
    state = db.Column(String(120))
    phone = db.Column(String(120))
    genres = db.Column(String(120))
    image_link = db.Column(String(500))
    facebook_link = db.Column(String(120))

    def __repr__(self):
       return "<Artist(name='%s', city='%s', state='%s', phone='%s', genres='%s', image_link='%s' facebook_link='%s')>" % \
              (self.name, self.city, self.state, self.phone, self.genres, self.image_link, self.facebook_link)
    def save(self):
        """ Saves an existing Category in the database """
        # if the id is None it hasn't been added to the database
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        """ Deletes a Category from the database """
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def init_db(cls):
        """ Initializes the database session """
        cls.logger.info('Artist: Initializing database')
        db.create_all()  # make our sqlalchemy tables

    @classmethod
    def delete_all(cls):
        cls.query.delete()
        db.session.commit()

    @classmethod
    def all(cls):
        """ Return all of the Categories in the database """
        cls.logger.info('Processing all Artists')
        return cls.query.all()

    @classmethod
    def find(cls, id):
        """ Find a Category by it's id """
        cls.logger.info('Processing Artist lookup for id %s ...', id)
        return cls.query.get(id)

    @classmethod
    def find_or_404(cls, id):
        """ Find a Category by it's id """
        cls.logger.info('Processing Artist lookup or 404 for id %s ...', id)
        return cls.query.get_or_404(id)

    @classmethod
    def find_by_name(cls, name):
        """ Query that finds Categories by their name """
        cls.logger.info('Processing Artist name query for %s ...', name)
        return cls.query.filter(Artist.name == name)

    # TODO: implement any missing fields, as a database migration using Flask-Migrate

# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.
