#!/usr/bin/python3
""" holds class User"""
from models.base_model import BaseModel, Base
import sqlalchemy
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


storecondition = getenv("HBNB_TYPE_STORAGE")


class User(BaseModel, Base):
    """Representation of a user """
    if storecondition == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", backref="user")
        reviews = relationship("Review", backref="user", cascade="all, delete",
                               passive_deletes=True)
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
