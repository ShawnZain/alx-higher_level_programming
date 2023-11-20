#!/usr/bin/python3

def safe_print_division(a, b):
    """divides 2 numbers provided as args
    Returns:
        The value after division
        Otherwise None
    """
    try:
       result = a / b
    except (TypeError, ZeroDivisionError, AttributeError):
        result = None
    finally:
        print("Inside result: {}".format(result))
    return (result)
