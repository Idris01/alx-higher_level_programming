#!/usr/bin/python3
"""Lookup Module

This module defines a single function "lookup(obj)"
that returns all attributes and method of an object "obj"

    Usage:
        lookup(obj)

"""


def lookup(obj):
    """Return list  attributes &  methods of an object

    Args:
        obj (object): Object of any type

    Returns:
        list of attributes and methods

    """

    return dir(obj)
