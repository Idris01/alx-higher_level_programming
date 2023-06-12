#!/usr/bin/python3
""" add_attribute Module
"""


def add_attribute(cls, name, value):
    """Add a given attribute "name" with "value" to cls

    Args:
        cls (object): an object belonging to any class
        name (str): attribute name
        value: attribute value

    Raise:
        TypeError: if attribute not added
    """
    if '__dict__' not in dir(cls):
        raise TypeError("can't add new attribute")

    cls.__dict__.__setitem__(name, value)
    if cls.__dict__.get(name, None) != value:
        raise TypeError("can't add new attribute")
