#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    for item in dir(hidden_4):
        if not item.startswith("__"):
            print("{}".format(item))
