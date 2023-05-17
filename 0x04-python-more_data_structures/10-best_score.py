#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    large_key = list(a_dictionary.keys())[0]
    large_value = a_dictionary[large_key]
    for key, val in a_dictionary.items():
        if large_value < val:
            large_value = val
            large_key = key
    return large_key
