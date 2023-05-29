#!/usr/bin/python3
def safe_print_integer(value):
    correct_print = True

    try:
        print("{:d}".format(value))
    except ValueError:
        correct_print = False
    return correct_print


if __name__ == "__main__":
    print(safe_print_integer("89"))
    print(safe_print_integer(89))
