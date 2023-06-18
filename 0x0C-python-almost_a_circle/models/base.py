#!/usr/bin/python3
"""This module define the Base class
"""

import json


class Base:
    """Base class

    Args:
        id (int): id of the instance

    Attributes:
        __nb_objects (int): number of active instance
        of the class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes instance by setting the id
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert list of dictionary to json format

        Args:
            list_dictionaries (list): list of dict

        Returns:
            json string representation

        """

        list_dict = list_dictionaries

        if list_dict is None or not list_dict:
            return "[]"

        return json.dumps(list_dict)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save objects contain in list_objs to file

        Args:
            list_objs (list): list of objects that are
            derived from Base

        """

        if list_objs is None or not list_objs:
            with open('Base.json', 'w', encoding='utf-8') as stream:
                stream.write("[]")
                return

        name = f"{type(list_objs[0]).__name__}.json"
        list_dict = [
                obj.to_dictionary() for
                obj in list_objs
                ]

        with open(name, 'w', encoding="utf-8") as f:
            f.write(cls.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """Convert from json to python list type

        Args:
            json_string (str): json string representation

        Returns:
            list of python dictionary
        """

        if json_string is None or not json_string:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create a new instance from dictionary

        Args:
            dictionary (dict): attrubutes of new object
        Returns:
            newly created instance of cls

        """

        if type(cls).__name__ != 'Base':
            new_obj = cls(2, 3)
        else:
            new_obj = cls()

        new_obj.update(**dictionary)

        return new_obj
