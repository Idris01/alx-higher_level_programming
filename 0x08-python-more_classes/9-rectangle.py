#!/usr/bin/python3
'''This module defines Rectangle class

Rectangle represents a normal rectangle with width and height
'''


class Rectangle:
    '''Represents a rectangle of size width X height

    Parameters:
        width (int): width of the rectangel
        height (int): height of the rectangle

    Attributes:
        number_of_instances (int): number of instances of Rectangle class
        print_symbol: used in printing string representation

    Usage:
        rec = Rectangle(5, 6)

    Raises:
        TypeError: if width or height is not an integer
        ValueError: if the width or height is less than 0

    '''
    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

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
        shape = [str(Rectangle.print_symbol) * self.width] * self.height
        return '\n'.join(shape)

    def __repr__(self):
        return 'Rectangle({}, {})'.format(self.width, self.height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''Finds  the Rectangle with bigger area between twp rectangles

        Args:
            rect_1 (Rectangle): first rectangle
            rect_2 (Rectangle): second rectangle
        Returns:
            rect_1 if larger or equal to rect_2 otherwise rect_2

        Raises:
            TypeError: if either rect_1 or rect_2 is not Rectangle

        '''
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

        @classmethod
        def square(cls, size=0):
            '''Creates a square of size
            Args:
                size (int): size of square

            Returns:
                new Rectangle with equal width and height
            '''
            return Rectangle(size, size)
