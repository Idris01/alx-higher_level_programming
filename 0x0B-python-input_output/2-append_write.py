#!/usr/bin/python3
""" The "append_write" module
"""


def append_write(filename="", text=""):
    """Append the content of text to filename

    If filename does not exist it is created

    Args:
        filename (str): name of file to append to
        text (str): content to append to filename

    Returns:
        num_appended (int): number of characters appended to filename
    """

    with open(filename, mode='a') as file_stream:
        num_appended = file_stream.write(text)

    return num_appended
