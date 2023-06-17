#!/usr/bin/python3
"""This module define the square class
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square shape

    Args:
        size (int): size of square
        x (int): distance from x axis
        y (int): distance from y axis
        id (int): id of square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the square
        """
        super().__init__(size, size, x=x, y=y, id=id)
        self.size = size

    def __str__(self):
        sqr_template = '[Square] ({}) {}/{} - {}'
        return sqr_template.format(
                self.id, self.x, self.y, self.size
                )

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size
        self._size = size
