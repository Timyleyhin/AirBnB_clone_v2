#!/usr/bin/python3
from models.base_model import BaseModel
"""
User class representation module
"""


class User(BaseModel):
    """
    Definition of class User that inherits from BaseModel
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
