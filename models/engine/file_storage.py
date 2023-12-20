#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
"""
File storage model responsible for serialization and deserialization
"""


class FileStorage:
    """
    file storage representation class
    """

    __file_path = "file.json"
    __objects = {}
    Classes = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review
            }

    def all(self):
        """
        Returns dictionary representation of an object
        """

        return FileStorage.__objects

    def new(self, obj):
        """
        sets object instances to __objects dictionary
        """

        obj_key = f"{type(obj).__name__}.{obj.id}"
        FileStorage.__objects[obj_key] = obj

    def save(self):
        """
        Serialize an __object in a JSON file
        """
        my_dict = {}
        for key, value in FileStorage.__objects.items():
            my_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        my_dict = {}
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                obj_dict = json.load(f)
                for k, v in obj_dict.items():
                    name, id = k.split(".")
                    my_dict[k] = self.Classes[name](**v)
                FileStorage.__objects = my_dict
        except FileNotFoundError:
            pass
