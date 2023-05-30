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
            print("{}".format("#" * self.size))
        else:
            if self.size == 0:
                print()


if __name__ == '__main__':
    my_square = Square(3)
    my_square.my_print()

    print("--")

    my_square.size = 10
    my_square.my_print()

    print("--")

    my_square.size = 0
    my_square.my_print()

    print("--")
