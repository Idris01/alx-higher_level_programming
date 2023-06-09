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

    def update(self, *args, **kwargs):
        """Update attributes of square

        Args:
            args (iterable): arguments for to update
            square attributes
            kwargs (dict): keyword arguments to update
            square attributes

        """

        attr = ['id', 'size', 'x', 'y']
        for idx, val in enumerate(args[:4]):
            self.__setattr__(attr[idx], val)

        if len(args) == 0:
            for key, value in kwargs.items():
                if key in attr:
                    self.__setattr__(key, value)

    def to_dictionary(self):
        """Return a dictionary of square attributes
        """

        attr_list = ['id', 'size', 'x', 'y']
        attr_map = self.__dict__

        attr = {key.split('_')[-1]: val for key, val in attr_map.items()}

        return {
                key: val for key, val
                in attr.items() if key in attr_list
                }
