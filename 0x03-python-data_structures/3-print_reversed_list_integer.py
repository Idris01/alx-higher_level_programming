#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for item in reversed(my_list):
        print("{:d}".format(item))
    if (len(my_list) == 0):
        print("")
