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
    cls.__dict__.__setitem__(name, value)
    if cls.__dict__.get(name, None) is not value:
        raise TypeError("can't add new attribute")
