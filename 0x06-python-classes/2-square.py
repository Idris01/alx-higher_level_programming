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

    def __init__(self, size=0):
        if not type(size) == int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size


if __name__ == '__main__':
    my_square_1 = Square(3)
    print(type(my_square_1))
    print(my_square_1.__dict__)

    my_square_2 = Square()
    print(type(my_square_2))
    print(my_square_2.__dict__)
