#!/usr/bin/python3
"""The "write_file" Module
"""


def write_file(filename="", text=""):
    """ Write text to a file filename

    If filename does not exist, it is created. If the filename
    already exist, the content is overwritten

    Args:
        filename (str): name of file to write to
        text (str): content to write to filename

    Returns:
        num_char (int): number of character written
    """

    with open(filename, mode='w', encoding='utf-8') as file_stream:
        num_char = file_stream.write(text)

    return num_char
