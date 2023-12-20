#!/usr/bin/python3
from datetime import datetime
from models.base_model import BaseModel
from models import storage
import io
import unittest
from unittest.mock import patch
"""
Unit test for base model
"""


class TestBaseModel(unittest.TestCase):
    """
    unit test class for base model
    """

    def test_basemodel_instance(self):
        """Assert is instance of base model"""

        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)

    def test_basemodel_id(self):
        """Assert that id work mormallY"""

        obj = BaseModel()
        obj_ids = obj.__dict__
        self.assertIn("id", obj_ids.keys())

        """Assert that id is a string"""

        id = obj_ids["id"]
        self.assertIsInstance(id, str)

        """Assert that id's are unique"""

        new_obj = BaseModel()
        new_obj_ids = new_obj.__dict__
        new_id = new_obj_ids["id"]

        self.assertNotEqual(id, new_id)

    def test_basemodel_created_at(self):
        """assert created_at is present"""

        obj = BaseModel()
        obj_dict = obj.__dict__
        self.assertIn("created_at", obj_dict.keys())

        """assert that created_at value is an object"""

        created_at = obj_dict["created_at"]
        self.assertIsInstance(created_at, datetime)

    def test_basemodel_updated_at(self):
        """assert updated_at is present"""

        obj = BaseModel()
        obj_dict = obj.__dict__
        self.assertIn("updated_at", obj_dict.keys())

        """assert that updated_at value is an object"""

        updated_at = obj_dict["updated_at"]
        self.assertIsInstance(updated_at, datetime)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_basemodel_str(self, mock_stdout):
        """assert that __str__ method returns the correct output"""

        obj = BaseModel()
        print(obj)

        printed_output = mock_stdout.getvalue()

        expected_output = f"[{type(obj).__name__}] ({obj.id}) {obj.__dict__}\n"

        self.assertEqual(printed_output, expected_output)

    def test_basemodel_save(self):
        """assert that updated_at value changes after calling save()"""

        obj = BaseModel()
        obj_dict = obj.__dict__
        updated_at = obj_dict["updated_at"]

        obj.save()
        new_updated_at = obj_dict["updated_at"]

        self.assertNotEqual(updated_at, new_updated_at)

    def test_basemodel_to_dict(self):
        """assert dictionary representation of an instance"""

        obj = BaseModel()
        obj_dict = obj.to_dict()

        self.assertIsInstance(obj_dict, dict)

        """assert that updated_at value is a string"""

        updated_at = obj_dict["updated_at"]
        self.assertIsInstance(updated_at, str)

        """assert that created_at value is a string"""

        created_at = obj_dict["created_at"]
        self.assertIsInstance(created_at, str)

        """assert that __class__ exist in the dictionary"""

        self.assertIn("__class__", obj_dict.keys())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_basemodel_kwargs(self, mock_stdout):
        """assert instance creation from kwargs"""

        obj = BaseModel()
        obj_dict = obj.to_dict()
        new_obj = BaseModel(**obj_dict)
        print(new_obj)

        printed_output = mock_stdout.getvalue()

        expected_output = f"[{type(obj).__name__}] ({obj.id}) {obj.__dict__}\n"

        self.assertEqual(printed_output, expected_output)

        """
        assert that normal instance creation and kwargs instance are the same
        """
        """reset the mock_stdout"""

        mock_stdout.truncate(0)
        mock_stdout.seek(0)

        print(obj)
        printed_output1 = mock_stdout.getvalue()

        expected_output = f"[{type(obj).__name__}] ({obj.id}) {obj.__dict__}\n"
        self.assertEqual(printed_output, printed_output1)

        """Assert that __class__ is not present in kwargs instances"""
        self.assertNotIn("__class__", printed_output)

    def test_obj_save(self):
        """
        tests method save of Storage class on BaseModel
        """

        my_obj = BaseModel()
        storage.save()
        my_obj_id = my_obj.id
        all_instances = storage.all()
        keys = ""
        for key in all_instances.keys():
            keys += key
        self.assertIn(my_obj_id, keys)
