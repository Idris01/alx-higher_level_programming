#!/usr/bin/python3
"""MyInt Module
"""


class MyInt(int):
    """MyInt is an Integer class that inverts equals and not equal comparision

    >>> my_int = MyInt(4)
    >>> my_int == 4
    False
    >>> my_int != 4
    True

    """

    def __eq__(self, value):
        """Return self!=value
        """
        return super().__ne__(value)

    def __ne__(self, value):
        """Return self==value
        """
        return super().__eq__(value)
