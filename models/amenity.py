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
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", backref="amenities")
        place_amenities = relationship(
            "Place",
            secondary="place_amenity",
            back_populates="amenities")
    else:
        name = ""
