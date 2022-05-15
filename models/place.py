#!/usr/bin/python3
""" Place Module for HBNB project """
import models
import sqlalchemy
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Float, ForeignKey, Integer, String, Table


class Place(BaseModel, Base):
    """ A place to stay """
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
