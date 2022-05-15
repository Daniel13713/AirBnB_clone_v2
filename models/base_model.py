#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import models
import sqlalchemy
import uuid
from os import getenv
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import time

if models.storecondition == "db":
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """A base class for all hbnb models"""
    if models.storecondition == "db":
        id = Column(String(60), nullable=False, primary_key=True)
        created_at = Column(
            DateTime, nullable=False, default=datetime.utcnow())
        updated_at = Column(
            DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at
            """storage.new(self)"""
        else:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            else:
                self.created_at = datetime.utcnow()
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
            else:
                self.updated_at = datetime.utcnow()
            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        new_dic = self.__dict__.copy()
        if "created_at" in new_dic:
            new_dic["created_at"] = new_dic["created_at"].strftime(time)
        if "updated_at" in new_dic:
            new_dic["updated_at"] = new_dic["updated_at"].strftime(time)
        new_dic["__class__"] = self.__class__.__name__

        if "_sa_instance_state" in new_dic:
            new_dic.pop("_sa_instance_state")

        return new_dic

    def delete(self):
        """
        ---------------------------------------------
        delete the current instance from the storage
        (models.storage) by calling the method delete
        ---------------------------------------------
        """
        pass


