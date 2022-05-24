#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import getenv


storecondition = getenv("HBNB_TYPE_STORAGE")


if storecondition == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    # print("In dbStorage")
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    # print("In file_storage")
storage.reload()
