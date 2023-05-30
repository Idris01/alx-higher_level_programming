#!/usr/bin/python3
'''Square module '''


class Square:
    '''Square class with private instance attribute "size" '''

    def __init__(self, size):
        self.__size = size


if __name__ == '__main__':
    my_square = Square(3)
    print(type(my_square))
    print(my_square.__dict__)

    try:
        print(my_square.size)
    except Exception as e:
        print(e)

    try:
        print(my_square.__size)
    except Exception as e:
        print(e)
