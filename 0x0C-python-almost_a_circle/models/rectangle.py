#!/usr/bin/python3
"""This midule define a Rectangle class
"""

from .base import Base


class Rectangle(Base):
    """Represents a Rectangle shape
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes instance of a Rectangle

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
            x (int): distace from x coordinate
            y (int): distance from y coordinate
            id (int): id of objec

        """

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Retrieve the width of rectangle"""
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        """Retrieve the height of rectangle"""
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height
