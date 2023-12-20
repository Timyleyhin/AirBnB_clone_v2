#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.place import Place

"""supplies unittest class for testing place class
"""


class TestState(unittest.TestCase):
    """
    Defines test methods for class place
    """
    def test_obj_instance(self):
        """Asserts that instance is place"""
        my_obj = Place()
        self.assertTrue(isinstance(my_obj, Place))

    def test_obj_attributes(self):
        """Asserts that attribute is set and of correct type"""
        my_obj = Place()
        self.assertTrue(isinstance(my_obj, Place))
        self.assertTrue(isinstance(my_obj.city_id, str))
        self.assertTrue(isinstance(my_obj.user_id, str))
        self.assertTrue(isinstance(my_obj.name, str))
        self.assertTrue(isinstance(my_obj.description, str))
        self.assertTrue(isinstance(my_obj.number_rooms, int))
        self.assertTrue(isinstance(my_obj.number_bathrooms, int))
        self.assertTrue(isinstance(my_obj.max_guest, int))
        self.assertTrue(isinstance(my_obj.price_by_night, int))
        self.assertTrue(isinstance(my_obj.latitude, float))
        self.assertTrue(isinstance(my_obj.longitude, float))
        self.assertTrue(isinstance(my_obj.amenity_ids, list))

    def test_state_parent(self):
        """Asserts that object inherits from BaseModel"""
        my_obj = Place()
        self.assertTrue(issubclass(type(my_obj), BaseModel))
