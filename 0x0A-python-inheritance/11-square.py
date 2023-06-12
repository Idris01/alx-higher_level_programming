#!/usr/bin/python3
""" Square Module
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a rectangle of size "size"

    Args:
        size (int): size of the square

    >>> square = Square(5)
    >>> square.area()
    25
    >>> print(square)
    [Square] 5/5
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
        Rectangle.__init__(self, size, size)
        self.__size = size

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
