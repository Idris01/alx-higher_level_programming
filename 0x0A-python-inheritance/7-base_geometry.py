#!/usr/bin/python3
""" This module define a python class called BaseGeometry
"""


class BaseGeometry:
    """Represents a simple Geometry
    """

    def area(self):
        """ Calculate the area of geometry
        """

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validates the data to generate a geometry

        Args:
            name (str): name of the geometry
            value (int): size of the geometry

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is <= 0
        """

        if not isinstance(value, int):
            raise TypeError("value must be an integer")

        if value <= 0:
            raise ValueError('value must be greater than 0')
