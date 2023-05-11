#!/usr/bin/python3
from sys import argv

arg_len = len(argv)
total = 0

if __name__ == "__main__":
    if arg_len == 1:
        print(0)
    else:
        for arg in argv[1:]:
            total += int(arg)
        print("{}".format(total))
