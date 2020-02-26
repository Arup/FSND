from flask_sqlalchemy import Model
from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Boolean, PickleType

class Venue(Model):
    __tablename__ = 'Venue'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    city = Column(String(120))
    state = Column(String(120))
    address = Column(String(120))
    phone = Column(String(120))
    image_link = Column(String(500))
    facebook_link = Column(String(120))

    def __repr__(self):
       return "<Artist(name='%s', city='%s', state='%s', phone='%s', genres='%s', image_link='%s' facebook_link='%s')>" % \
              (self.name, self.city, self.state, self.phone, self.genres, self.image_link, self.facebook_link)
    # TODO: implement any missing fields, as a database migration using Flask-Migrate

class Artist(Model):
    __tablename__ = 'Artist'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    city = Column(String(120))
    state = Column(String(120))
    phone = Column(String(120))
    genres = Column(String(120))
    image_link = Column(String(500))
    facebook_link = Column(String(120))

    def __repr__(self):
       return "<Artist(name='%s', city='%s', state='%s', phone='%s', genres='%s', image_link='%s' facebook_link='%s')>" % \
              (self.name, self.city, self.state, self.phone, self.genres, self.image_link, self.facebook_link)

    # TODO: implement any missing fields, as a database migration using Flask-Migrate

# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.
