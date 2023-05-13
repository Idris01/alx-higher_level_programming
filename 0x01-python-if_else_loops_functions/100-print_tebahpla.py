#!/usr/bin/python3
for i in range(ord("Z"), ord("A") - 1, -1):
    print("{}".format(chr(i + (32 if i % 2 == 0 else 0))), end="")
