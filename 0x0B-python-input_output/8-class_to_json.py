#!/usr/bin/python3
"""This module define the "class_to_json" function
"""


def class_to_json(obj):
    """Return dictionary description of attributes of obj

    Args:
        obj (object): instance of a class to get attribute of
    """

    if '__dict__' in dir(obj):
        return obj.__dict__
    return {}
