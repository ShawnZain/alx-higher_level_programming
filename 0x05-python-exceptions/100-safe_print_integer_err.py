#!/usr/bin/python3

import sys

def safe_print_integer_err(value):
    """prints integer value passed as argument

    Args:
        value (int): value can be of any type
        we test if it is an int

    Return:
        Prints the int if its an int and returns True
        Prints to stderr the exception and returns False
    """

    try:
        print("{:d}".format(value))
        return (True)
    except Exception as e:
        print("Exception: {}".format(e), file = sys.stderr)
        return (False)

