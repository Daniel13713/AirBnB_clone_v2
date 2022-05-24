#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    """Change made from def all(self) to def all(self, cls=None)"""

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is None:
            return FileStorage.__objects
        else:
            class_name = cls.__name__
            class_objects = {}
            for key, value in FileStorage.__objects.items():
                if class_name == key.split(".")[0]:
                    class_objects.update({key: value})
            return class_objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict.update({key: value.to_dict()})

        with open(self.__file_path, mode="w+", encoding="utf-8") as file:
            json.dump(new_dict, file)

    def reload(self):
        """
        ------------------------------------------
        Loads storage dictionary from file
        Deserializing the JSON file to objects
        JSON -> OBJECT_PYTHON (deserializing)
        ------------------------------------------
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review,
        }

        try:
            with open(self.__file_path, mode="r", encoding="utf-8") as file:
                json_string = json.load(file)
                for key, value in json_string.items():
                    a = classes[value["__class__"]](**value)
                    new_dict = {key: a}
                    self.__objects.update(new_dict)
        except Exception:
            pass

    def delete(self, obj=None):
        """delete obj from __objects if it is inside"""
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """
        ---------------------------------------
        Call deserilization reaload() method
        ---------------------------------------
        """

        self.reload()
