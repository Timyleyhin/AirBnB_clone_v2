#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity

"""supplies unittest class for testing Amenity class
"""


class TestAmenity(unittest.TestCase):
    """
    Defines test methods for class State
    """
    def test_obj_instance(self):
        """Asserts that instance is Amenity"""
        my_obj = Amenity()
        self.assertTrue(isinstance(my_obj, Amenity))

    def test_obj_attribute(self):
        """Asserts that attribute is set and of string type"""
        my_obj = Amenity()
        self.assertTrue(isinstance(my_obj.name, str))

    def test_obj_parent(self):
        """Asserts that object inherits from BaseModel"""
        my_obj = Amenity()
        self.assertTrue(issubclass(type(my_obj), BaseModel))
