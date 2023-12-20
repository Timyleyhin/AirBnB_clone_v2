#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.state import State

"""supplies unittest class for testing State class
"""


class TestState(unittest.TestCase):
    """
    Defines test methods for class State
    """
    def test_obj_instance(self):
        """Asserts that instance is State"""
        my_obj = State()
        self.assertTrue(isinstance(my_obj, State))

    def test_obj_attribute(self):
        """Asserts that attribute is set and of string type"""
        my_obj = State()
        self.assertTrue(isinstance(my_obj.name, str))

    def test_obj_parent(self):
        """Asserts that object inherits from BaseModel"""
        my_obj = State()
        self.assertTrue(issubclass(type(my_obj), BaseModel))
