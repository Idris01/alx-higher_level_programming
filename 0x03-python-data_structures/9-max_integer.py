#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    large = my_list[0]
    for num in my_list[1:]:
        if num > large:
            large = num
    return large
