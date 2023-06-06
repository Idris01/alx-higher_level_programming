#!/usr/bin/python3
'''This module defines Rectangle class

Rectangle represents a normal rectangle with width and height
'''


class Rectangle:
    '''Represents a rectangle of size width X height

    Parameters:
        width (int): width of the rectangel
        height (int): height of the rectangle

    Usage:
        rec = Rectangle(5, 6)

    Raises:
        TypeError: if width or height is not an integer
        ValueError: if the width or height is less than 0

    '''
    def __init__(self, width=0, height=0):
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')

        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')

        self.__width = width
        self.__height = height

    @property
    def width(self):
        "Return the width of the Rectangle"
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError('width must be an integer')

        if width < 0:
            raise ValueError('width must be >= 0')

        self.__width = width

    @property
    def height(self):
        "Return the height of the Rectangle"
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError('height must be an integer')

        if height < 0:
            raise ValueError('height must be >= 0')

        self.__height = height

    def area(self):
        "Return the area of the Rectangle"
        return self.__width * self.__height

    def perimeter(self):
        "Return the perimeter of the Rectangle"
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        shape = ["#" * self.width] * self.height
        return '\n'.join(shape)

    def __repr__(self):
        return 'Rectangle({}, {})'.format(self.width, self.height)

    def __del__(self):
        print("Bye rectangle...")
