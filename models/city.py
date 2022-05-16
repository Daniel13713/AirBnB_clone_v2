#!/usr/bin/python3
""" City Module for HBNB project """
import models
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship


storecondition = getenv("HBNB_TYPE_STORAGE")


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    if storecondition == "db":
        __tablename__ = "cities"
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship("Place", backref="cities")
    else:
        state_id = ""
        name = ""
