#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = [0] * list_length
    counter = 0

    while (counter < list_length):
        try:
            new_list[counter] = my_list_1[counter] / my_list_2[counter]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            counter += 1
    return new_list


if __name__ == "__main__":
    list1 = [1, 2, 4, 5]
    list2 = [None, 2, 0, 6, "idris"]
    print("new List is {}".format(list_division(list1, list2, 5)))
