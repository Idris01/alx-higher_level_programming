#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

arg_len = len(sys.argv)

if __name__ == "__main__":
    if arg_len < 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    op_map = {
            "+": add,
            "-": sub,
            "*": mul,
            "/": div
            }
    operator = sys.argv[2]
    if operator not in op_map.keys():
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    print("{} {} {} = {}".format(a, operator, b, op_map[operator](a, b)))
