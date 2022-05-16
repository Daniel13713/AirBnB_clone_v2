#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
import models


class Review(BaseModel, Base):
    """ Review classto store review information """
    if models.storecondition == "db":
        __tablename__ = "reviews"
    else:
        place_id = ""
        user_id = ""
        text = ""
