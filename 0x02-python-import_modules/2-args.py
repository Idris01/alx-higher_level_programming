#!/usr/bin/python3
from sys import argv

arg_size = len(argv)

if __name__ == "__main__":
    if arg_size == 1:
        print("{} arguments.".format(0))
    else:
        if arg_size == 2:
            print("{} argument:".format(1))
        else:
            print("{} arguments:".format(arg_size - 1))

        for index, value in enumerate(argv[1:]):
            print("{}: {}".format(index + 1, value))
