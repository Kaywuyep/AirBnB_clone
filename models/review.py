#!/usr/bin/python3
"""Review class that inherits from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """A simple Review class, to check other classes"""
    place_id = ""
    user_id = ""
    text = ""
