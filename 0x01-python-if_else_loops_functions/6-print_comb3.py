#!/usr/bin/python3
for low in range(0, 10):
    for high in range(low+1, 10):
        if (low == 8) and (high == 9):
            print("{}{}".format(low, high))
        else:
            print("{}{}".format(low, high), end=", ")
