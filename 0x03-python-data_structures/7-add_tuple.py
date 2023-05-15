#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    x, y, a, b = (0, 0, 0, 0)

    if len(tuple_a) == 1:
        a = tuple_a[0]
    elif len(tuple_a) > 1:
        a, b = tuple_a[:2]
    if len(tuple_b) == 1:
        x = tuple_b[0]
    elif len(tuple_b) > 1:
        x, y = tuple_b[:2]

    return (x + a, y + b)
