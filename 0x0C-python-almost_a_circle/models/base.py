#!/usr/bin/python3
"""This module define the Base class
"""


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
