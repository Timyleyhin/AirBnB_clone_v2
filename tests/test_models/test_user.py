#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.user import User

"""supplies unittest class for testing User class
"""


class TestUser(unittest.TestCase):
    """
    Defines test methods for class User
    """
    def test_obj_instance(self):
        """Asserts that instance is user"""
        my_obj = User()
        self.assertTrue(isinstance(my_obj, User))

    def test_obj_attribute(self):
        """Asserts that attribute is set and of string type"""
        my_obj = User()
        self.assertTrue(isinstance(my_obj.email, str))
        self.assertTrue(isinstance(my_obj.password, str))
        self.assertTrue(isinstance(my_obj.first_name, str))
        self.assertTrue(isinstance(my_obj.last_name, str))

    def test_obj_parent(self):
        """Asserts that object inherits from BaseModel"""
        my_obj = User()
        self.assertTrue(issubclass(type(my_obj), BaseModel))
