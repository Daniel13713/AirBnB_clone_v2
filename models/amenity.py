#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import models
from os import getenv


storecondition = getenv("HBNB_TYPE_STORAGE")


class Amenity(BaseModel, Base):
    if storecondition == "db":
        __tablename__ = "amenities"
    else:
        name = ""
