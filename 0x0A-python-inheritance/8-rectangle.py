#!/usr/bin/python3
"""Rectangle module
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle of width by height

    Args:
        width (int): width of the rectangle
        height (int): height of the rectangle

        >>> rectangle = Rectangle(5, 6)
        >>> rectangle.width
        Traceback (most recent call last):
            ...
        AttributeError: 'Rectangle' object has no attribute 'width'
        >>> Rectangle('5', 6)
        Traceback (most recent call last):
            ...
        TypeError: width must be an integer
        >>> Rectangle(5, '6')
        Traceback (most recent call last):
            ...
        TypeError: height must be an integer
        >>> Rectangle() # doctest: +ELLIPSIS
        Traceback (most recent call last):
            ...
        TypeError: ... missing 2 required positional arguments: ...

    """

    def __init__(self, width, height):
        BaseGeometry.__init__(self)
        self.integer_validator('width', width)
        self.integer_validator('height', height)

        self.__width = width
        self.__height = height
