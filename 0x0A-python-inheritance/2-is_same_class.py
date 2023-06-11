#!/usr/bin/python3


def is_same_class(obj, a_class):
    """Checks if obj is instance of a_class

    Args:
        obj: object of any class
        a_class: any class

    Returns:
        Boolean True if obj is instance of a_class
        otherwise False

    """

    return type(obj).__name__ == a_class.__name__
