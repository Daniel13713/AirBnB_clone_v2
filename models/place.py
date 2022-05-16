#!/usr/bin/python
""" holds class Place"""
from subprocess import list2cmdline
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table, all_
from models.review import Review
from sqlalchemy.orm import relationship


storecondition = getenv("HBNB_TYPE_STORAGE")

if storecondition == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'), primary__key=True), 
    Column('amenity_id', String(60), ForeignKey('amenities.id'), primary__key=True))



class Place(BaseModel, Base):
    """ A place to stay """
    if storecondition == 'db':
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship(
            "Review",
            backref="place",
            cascade="all, delete",
            passive_deletes=True)
        amenities = relationship("Amenity", secondary="place_amenity", backref="place_amenities", viewonly=False)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """Returns a list of City instances with state_id equals
            to the current State.id"""
            reviewlist = []
            allreviews = models.storage.all(Review)
            for review in allreviews.values():
                if review.review_id == self.id:
                    reviewlist.append(review)
            return reviewlist

        @property
        def amenities(self):
            """Returns the list of amenities"""
            from models.amenity import Amenity
            list_amenities = []
            all_amenities = models.storage.all(Amenity)
            for amenity in all_amenities.values():
                if amenity.place_id == self.id:
                    list_amenities.append(amenity)
            return list_amenities
