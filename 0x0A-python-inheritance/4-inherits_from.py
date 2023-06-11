#!/usr/bin/python3
""" This module define the 'inherits_from(obj, a_class)' function
"""


def inherits_from(obj, a_class):
    """Checks if obj is an instance of subclass of a_class

    The obj can be an instance of a class that directly or indirectly
    inherits from a_class

    Args:
        obj: object to check instance of
        a_class: class to make check on

    """

    return (issubclass(type(obj), a_class) and
            type(obj).__name__ is not a_class.__name__)
