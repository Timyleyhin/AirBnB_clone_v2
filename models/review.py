#!/usr/bin/python3
from models.base_model import BaseModel
"""
Review class representation module
"""


class Review(BaseModel):
    """
    Definition of class Review that inherits from BaseModel
    """

    place_id = ""
    user_id = ""
    text = ""
