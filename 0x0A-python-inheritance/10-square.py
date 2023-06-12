#!/usr/bin/python3
""" This module defines a python class Square
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a Square of size "size"

    Args:
        size (int): size of the square

    >>> square = Square(5)
    >>> square.area()
    25
    >>> print(square)
    [Rectangle] 5/5
    >>> Square('5')
    Traceback (most recent call last):
        ...
    TypeError: width must be an integer
    >>> Square(-5)
    Traceback (most recent call last):
        ...
    ValueError: width must be greater than 0

    """

    def __init__(self, size):
        """ initialize Square with size
        """

        Rectangle.__init__(self, size, size)
        self.__size = size

    def area(self):
        """Return area of square
        """

        return self.__size * self.__size
