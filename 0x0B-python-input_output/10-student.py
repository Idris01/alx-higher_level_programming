#!/usr/bin/python3
""" This module defines student class
"""


class Student:
    """STudent class

    Args:
        first_name (str): first name of student
        last_name (str): last name of student
        age (int): age of student
    """

    def __init__(self, first_name, last_name, age):
        """initializes the student object
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrive the dictionary of attrs of student
        """
        if (attrs and type(attrs) == list):
            return {key: self.__dict__[key] for key in attrs if
                    key in self.__dict__}
        return self.__dict__
