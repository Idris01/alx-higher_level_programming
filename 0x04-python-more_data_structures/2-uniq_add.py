#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = list(set(my_list))
    num = 0
    for item in unique:
        num += item
    return num
