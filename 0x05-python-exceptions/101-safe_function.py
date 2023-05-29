#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        ans = fct(*args)
        return ans
    except Exception as exp:
        sys.stderr.write("Exception: {}\n".format(exp))
        return None


if __name__ == "__main__":
    def add(*arg):
        total = 0
        for i in arg:
            total += i
        return total
    print("total is {}".format(safe_function(add, 1, 2, 3, 4)))
    print("total is {}".format(safe_function(add, 1, 2, "aee", 3, 4)))
