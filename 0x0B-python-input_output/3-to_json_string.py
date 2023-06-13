#!/usr/bin/python3
""" This module define 'to_json_string'
"""

import json


def to_json_string(my_obj):
    """Convert my_obj to json notation

    Args:
        my_obj (str): the string to convert to json

    Returns:
        json representation of the string

    """

    return json.dumps(my_obj)
