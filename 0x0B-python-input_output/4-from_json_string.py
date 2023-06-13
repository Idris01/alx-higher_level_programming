#!/usr/bin/python3
""" This module define the 'from_json_string' function
"""
import json


def from_json_string(my_str):
    """Convert json to python object

    Args:
        my_str: the json representation to change to python object

    Returns:
        python object representation
    """
    return json.loads(my_str)
