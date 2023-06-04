#!/usr/bin/python3
""" The say_my_name module that prints full name

This module consists of a single function 'say_my_name that recieves
one positional argument 'first_name' and an optional argument last_name"
"""


def say_my_name(first_name, last_name=""):
    '''Prints the full name

    Args:
        first_name (str): the first name
        last_name (str): the last name

    Returns:
        Nothing
    '''

    if type(first_name) is not str or first_name.strip() == '':
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print('My name is {} {}'.format(first_name.strip(), last_name.strip()))
