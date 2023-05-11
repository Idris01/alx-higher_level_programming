#!/usr/bin/python3
from sys import argv

arg_size = len(argv)

if __name__ == "__main__":
    if arg_size == 1:
        print("0 argument.")
    else:
        if arg_size == 2:
            print("1 argument:")
        else:
            print("{} arguments:".format(arg_size - 1))

        for index, value in enumerate(argv[1:]):
            print("{}: {}".format(index + 1, value))
