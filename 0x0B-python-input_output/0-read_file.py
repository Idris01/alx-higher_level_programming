#!/usr/bin/python3
""" The "read_file" module
"""


def read_file(filename=""):
    """Read content of a given filename and print to stdout
 
    Args:
        filename (str): name of file to read

    """

    with open(filename, encoding='utf-8') as file_stream:
        print(file_stream.read())
