#!/usr/bin/python3

def safe_print_integer(value):
    """checks if input is an integer
    it will print the int

    Args:
        value (int): value to check if it is int

    Return:
        True if it is int
        False it is not
    """

    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
