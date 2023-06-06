#!/usr/bin/python3
''' Define a text_indentationnl function'''


def text_indentation(text):
    '''Print formated text

    For a given text, after each of symbol "."
    , ':' and "!", "\n\n" is inserted to put
    a new line and a blank line

    Args:
        text (str): text to indent

    Returns:
        Nothing
    '''

    if type(text) != str:
        raise TypeError('text must be a string')

    text = text.strip()

    # replace "." with \n\n
    text = text.replace(".", ".\n\n")

    # replace ":" with \n\n
    text = text.replace(":", ":\n\n")

    # replace "?" with \n\n
    text = text.replace("?", "?\n\n")
    text = [txt.strip() for txt in text.split("\n\n")]
    print("{}".format("\n\n".join(text)), end="")


if __name__ == "__main__":
    text = """ I am a Software Engineer:,\
            I love what I do. what about you?\
            really!!"""
    text_indentation(text)
