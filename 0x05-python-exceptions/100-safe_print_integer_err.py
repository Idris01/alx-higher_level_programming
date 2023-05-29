#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    correct_print = True

    try:
        print("{:d}".format(value))
    except (TypeError, ValueError) as err:
        correct_print = False
        sys.stderr.write("Exception: {}\n".format(err))
    return correct_print


if __name__ == "__main__":
    print(safe_print_integer_err("ade"))
    print(safe_print_integer_err(None))
    print(safe_print_integer_err(-89))
