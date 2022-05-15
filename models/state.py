#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models import storage
from models.city import City
import models


class State(BaseModel, Base):
    """ State class """
    if models.storecondition == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="states", cascade="all")
    else:
        name = ""

    if models.storecondition != "db":
        @property
        def cities(self):
            """Returns a list of City instances with state_id equals
            to the current State.id"""
            citylist = []
            allcitys = storage.all(City)
            for city in allcitys.values():
                if city.state_id == self.id:
                    citylist.append(city)
            return citylist
