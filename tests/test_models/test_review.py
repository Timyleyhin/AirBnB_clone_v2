#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.review import Review

"""supplies unittest class for testing Review class
"""


class TestReview(unittest.TestCase):
    """
    Defines test methods for class review
    """
    def test_obj_instance(self):
        """Asserts that instance is revire"""
        my_obj = Review()
        self.assertTrue(isinstance(my_obj, Review))

    def test_obj_attribute(self):
        """Asserts that attribute is set and of string type"""
        my_obj = Review()
        self.assertTrue(isinstance(my_obj.text, str))

    def test_obj_parent(self):
        """Asserts that object inherits from BaseModel"""
        my_obj = Review()
        self.assertTrue(issubclass(type(my_obj), BaseModel))
