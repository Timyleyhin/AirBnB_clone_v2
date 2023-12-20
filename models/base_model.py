#!/usr/bin/python3
from datetime import datetime
import uuid
import models
"""
This module supplies a single class Basemodel defined with
attributes and methods
"""


class BaseModel:
    """
    Defines a Basemode class with attributes and methods
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the class
        """
        if args:
            return
        elif kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at":
                    self.created_at = datetime.fromisoformat(value)
                elif key == "updated_at":
                    self.updated_at = datetime.fromisoformat(value)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the instance
        [<class name>] (<self.id>) <self.__dict__>
        """

        string_rep = f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

        return (string_rep)

    def save(self):
        """
        updates the attribute updated_at to now
        """

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary representation of the instance
        """

        dict_rep = self.__dict__.copy()
        dict_rep["created_at"] = dict_rep["created_at"].isoformat()
        dict_rep["updated_at"] = dict_rep["updated_at"].isoformat()
        dict_rep["__class__"] = type(self).__name__

        return (dict_rep)
