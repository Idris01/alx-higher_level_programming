#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num_printed = 0
    counter = 0
    try:
        while (counter < x):
            print("{}".format(my_list[counter]), end="")
            num_printed += 1
            counter += 1
    except IndexError:
        pass
    finally:
        print()
        return num_printed


if __name__ == '__main__':
    my_list = [1, 2, 3, "ade"]
    print("num of items printed is {}".format(safe_print_list(my_list, 20)))
