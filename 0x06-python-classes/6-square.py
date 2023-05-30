#!/usr/bin/python3
'''Square module that define square shape'''


class Square:
    '''Represents Square Shape class

    Args:
        size (:obj:`int`, optional): size of the square

    Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than zero
    '''

    def __init__(self, size=0, position=(0, 0)):
        try:
            point_1, point_2 = position
            if type(point_1) != int or type(point_2) != int:
                raise TypeError
            if point_1 < 0 or point_2 < 0:
                raise TypeError
        except Exception:
            raise TypeError("position myst b a tuple of 2 positive integers")
        self.__position = position
        if not type(size) == int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    @property
    def size(self):
        '''Return the value of size'''
        return self.__size

    @size.setter
    def size(self, size):
        if not type(size) == int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self) -> int:
        '''Computes and returns area of the square'''

        return self.__size * self.__size

    def my_print(self):
        "Prints a square shape using # symbol"
        for i in range(self.size):
            print("{}{}".format(" " * self.position[0], "#" * self.size))
        else:
            if self.size == 0:
                print()

    @property
    def position(self):
        '''Gets the coordinate of a given square'''

        return self.__position

    @position.setter
    def position(self, position):
        try:
            point_1, point_2 = position
            if type(point_1) != int or type(point_2) != int:
                raise TypeError
            if point_1 < 0 or point_2 < 0:
                raise TypeError
        except Exception:
            raise TypeError("position myst b a tuple of 2 positive integers")
        self.__position = position


if __name__ == '__main__':
    my_square_1 = Square(3)
    my_square_1.my_print()

    print("--")

    my_square_2 = Square(3, (1, 1))
    my_square_2.my_print()

    print("--")

    my_square_3 = Square(3, (3, 0))
    my_square_3.my_print()

    print("--")
