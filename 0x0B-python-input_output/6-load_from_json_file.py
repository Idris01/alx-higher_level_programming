#!/usr/bin/python3
"""This module define the "load_from_json_file" function
"""

import json


def load_from_json_file(filename):
    """Loads a python object from given file "filename"

    Args:
        filename (str): name of file to read from

    Returns:
        new_object (object): loaded python object

    """

    with open(filename, mode='r', encoding='utf-8') as file_stream:
        new_object = json.loads(file_stream.read())

    return new_object
