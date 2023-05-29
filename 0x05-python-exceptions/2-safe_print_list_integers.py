#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num_printed = 0
    counter = 0

    while(counter < x):
        try:
            print("{:d}".format(my_list[counter]), end="")
            counter += 1
            num_printed += 1
            if counter == x:
                print()  # add newline
        except (ValueError, TypeError):
            counter += 1
            if counter == x:
                print()  # add newline
            continue
    return num_printed


if __name__ == "__main__":
    my_list = [1, 2, "ade", None, 3]
    print("Num Printed is {}".format(safe_print_list_integers(my_list, 5)))
