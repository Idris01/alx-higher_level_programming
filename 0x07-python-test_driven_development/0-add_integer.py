#!/usr/bin/python3
"""Defines the add_integer function"""


def add_integer(a, b=98):
    """Adds integer a and b

    Args:
        a (int or float) : first number
        b (int or float) : second number

    Returns:
        int sum of a and b
    """
    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    if type(b) not in (int, float):
        raise TypeError('b must be an integer')

    return int(a) + int(b)
