#!/usr/bin/python3
"""This module defines a class User"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
