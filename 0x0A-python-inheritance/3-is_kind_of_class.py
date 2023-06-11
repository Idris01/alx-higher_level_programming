#!/usr/bin/python3
""" is_kind_of_class module
"""


def is_kind_of_class(obj, a_class):
    """Checks if obj either obj is an instance of a_class or its subclass

    Args:
        obj: object of any class
        a_class: any given class

    Returns:
        Boolean: True if yes otherwise False

    """
    return isinstance(obj, a_class) or issubclass(type(obj), a_class)
