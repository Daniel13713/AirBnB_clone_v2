#!/usr/bin/python3
"""This module defines a class to manage Database of Mysql for hbnb clone"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os
from models.base_model import Base
"""from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review"""


class DBStorage():
    """
    -----------------------------------------------------------
    This class manages storage of hbnb models in Mysql Database
    -----------------------------------------------------------
    """

    """classes = {
        'BaseModel': BaseModel, 'User': User, 'Place': Place,
        'State': State, 'City': City, 'Amenity': Amenity,
        'Review': Review
    }"""

    __engine = None
    __session = None

    def __init__(self):
        """Instanciatize objects"""

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                os.getenv("HBNB_MYSQL_USER"),
                os.getenv("HBNB_MYSQL_PWD"),
                os.getenv("HBNB_MYSQL_HOST"),
                os.getenv("HBNB_MYSQL_DB")
            ), pool_pre_ping=True)
        # Base.metadata.create_all(self.__engine)
        # self.__session = sessionmaker(bind=self.__engine)

        """
        -----------------------------------
        drop all tables if the environment
        variable HBNB_ENV is equal to test
        -----------------------------------
        """
        if os.getenv("HBNB_ENV") == "test":
            with self.__session as session:
                session.drop_all(self.__engine, checkfirst=True)

    def all(self, cls=None):
        """
        --------------------------------------------------------
        query on the current database session (self.__session)
        all objects depending of the class name (argument cls)
        if cls=None, query all types of objects
        this method must return a dictionary
        --------------------------------------------------------
        """
        session = self.__session()
        new_dic = {}

        if cls is None:
            return self.__session.query()
        else:
            return self.__session.query(cls).all()

    def new(self, obj):
        """
        ---------------------------------------------------------------
        add the object to the current database session (self.__session)
        ---------------------------------------------------------------
        """
        self.__session.add(obj)
        # session.commit()

    def save(self):
        """
        ---------------------------------------------------------------
        Saves all changes of the current database session
        ---------------------------------------------------------------
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        ---------------------------------------------------------------
        deletes from the current database session obj if not None
        ---------------------------------------------------------------
        """
        with self.__session() as session:
            if obj is not None:
                session.delete(obj)
                session.commit()

    def reload(self):
        """
        ---------------------------------------------------------------
        Reloads data from the database
        ---------------------------------------------------------------
        """
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """
        ---------------------------------------------------------------
        Calls remove() on the private session
        ---------------------------------------------------------------
        """
        self.__session.remove()
