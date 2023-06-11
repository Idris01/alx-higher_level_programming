#!/usr/bin/python3
""" my_list module that define a single class MyList
"""


class MyList(list):
    """ subclass of list  that implements print_sorted function

    The MyList class extends the standard python list class but include an
    additional method "print_sorted" that takes no argument to prints the
    sorted form of the list without mutating the list

    Usage:
        my_list = MyList([1, 7, 3, 5])
        my_list.print_sorted()
            output : [1, 3, 5, 7]
    """

    def print_sorted(self, *args):
        """prints sorted form of list

        Raises:
            TyoeError: if argument is provided
        """

        if len(args) != 0:
            raise TypeError(f"MyList.print_sorted()\
                    takes no argument: got {len(args)}")
        print([i for i in sorted(self.copy())])
