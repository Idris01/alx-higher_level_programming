#!/usr/bin/python3
"""This module define the "save_to_json_file" function
"""

import json


def save_to_json_file(my_obj, filename):
    """Save a given json my_obj to filename

    Args:
        my_obj: the content to write
        filename (str): the file name to write to

    """

    with open(filename, mode='w', encoding='utf-8') as file_stream:
        file_stream.write(json.dumps(my_obj))
