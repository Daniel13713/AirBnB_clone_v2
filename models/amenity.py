#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import models


class Amenity(BaseModel, Base):
    if models.storecondition == "db":
        __tablename__ = "amenities"
    else:
        name = ""
