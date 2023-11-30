#!/usr/bin/python3

"""Defining the function"""


def add_integer(a, b=98):
    """A function that adds 2 integers or floats
    a and b must be either a float or an integer
        raise TypeError a must be an integer
        raise TypeError b must be an integer

    cast a and b to integers before adding them

    Return:
        an integer after adding a + b
    """

    if not isinstance(a, int) or not isinstance(a, float):
        raise TypeError('a must be an integer')
    elif not isinstance(b, int) or not isinstance(b, float):
        raise TypeError('b must be an integer')

    return int(a + b)
