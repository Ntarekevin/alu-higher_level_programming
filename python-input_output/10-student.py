#!/usr/bin/python3

"""Module"""


class Student:
    """Class"""

    def __init__(self, first_name, last_name, age):
        """Function"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

def to_json(self, attrs=None):
        """Function"""
        if isinstance(attrs, list) and all(
            isinstance(attr, str) for attr in attrs
        ):
            return {
                key: getattr(self, key) for key in attrs if hasattr(self, key)
            }
        return self.__dict__
