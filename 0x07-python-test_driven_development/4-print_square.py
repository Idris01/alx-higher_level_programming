#!/usr/bin/python3
"""Define a print_square function that prints square using # symbol
"""

def print_square(size):
    '''Prints a square of size using # symbol
    
    Args:
        size (int): size of the square
    
    Returns:
        Nothing
    '''

    if type(size) not in (int, float) or \
            (type(size) == float and (size // 1) < 0):
        raise TypeError('size must be an integer')

    if size < 0:
        raise ValueError('size must be >= 0')

    for row in range(int(size)):
        print("{}".format("#" * int(size)))

