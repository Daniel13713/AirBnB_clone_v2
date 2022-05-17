#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


storecondition = getenv("HBNB_TYPE_STORAGE")


class Amenity(BaseModel, Base):
    if storecondition == "db":
        from models.place import place_amenity
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
        place_amenities = relationship(
            "Place",
            secondary='place_amenity',
            backref="amenities")
    else:
        name = ""
