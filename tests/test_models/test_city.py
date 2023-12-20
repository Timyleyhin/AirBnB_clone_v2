#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.city import City

"""supplies unittest class for testing city class
"""


class TestClass(unittest.TestCase):
    """
    Defines test methods for class city
    """
    def test_obj_instance(self):
        """Asserts that instance is city"""
        my_obj = City()
        self.assertTrue(isinstance(my_obj, City))

    def test_obj_attributes(self):
        """Asserts that attribute is set and of string type"""
        my_obj = City()
        self.assertTrue(isinstance(my_obj.name, str))
        self.assertTrue(isinstance(my_obj.state_id, str))

    def test_obj_parent(self):
        """Asserts that object inherits from BaseModel"""
        my_obj = City()
        self.assertTrue(issubclass(type(my_obj), BaseModel))
