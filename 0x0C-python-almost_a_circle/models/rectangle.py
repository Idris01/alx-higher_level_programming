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
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')
        if type(x) is not int:
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        if type(y) is not int:
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')

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
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        self.__width = width

    @property
    def height(self):
        """Retrieve the height of rectangle"""
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')
        self.__height = height

    @property
    def x(self):
        """Retrieve the x of rectangle"""
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        self.__x = x

    @property
    def y(self):
        """Retrieve the y of rectangle"""
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')

        self.__y = y

    def area(self):
        """Return the area of rectangle
        """
        return self.width * self.height

    def display(self):
        """Prints the representation of rectangle using '#' symbol
        """
        if self.y > 0:
            print('\n' * self.y, end='')
        shape = '\n'.join(
                [((' ' * self.x) + ('#' * self.width))
                    for i in range(self.height)]
                )
        print(shape)

    def __str__(self):
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(
                self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Update attribute of a rectangle
        """
        attr = ['id', 'width', 'height', 'x', 'y']

        for index, value in enumerate(args[:5]):
            self.__setattr__(attr[index], value)

        if len(args) == 0:  # run only if args is not empty
            for key, val in kwargs.items():
                if key in attr:
                    self.__setattr__(key, val)

    def to_dictionary(self):
        """Return a dictionary of rectangle attributes
        """

        attr_map = self.__dict__

        return {key.split('_')[-1]: val for key, val in attr_map.items()}
