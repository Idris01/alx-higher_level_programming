#!/usr/bin/python3
def safe_print_division(a, b):
    result = None

    try:
        result = a / b
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(result))
    return result


if __name__ == "__main__":
    a, b = 12, 0
    print("The result of {} / {} = {}".format(a, b, safe_print_division(a, b)))
    a, b = 12, 2
    print("The result of {} / {} = {}".format(a, b, safe_print_division(a, b)))
