#!/usr/bin/python3

import sys

def safe_function(fct, *args):
    """prevents the function from returning errors

    Args:
        fct (pointer): pointer to a function
        *args (str): string with arguments to pass to fct

    Return:
        Result of the function if it successfully executed
        Otherwise prints error message to stderr and returns
        None
    """

    try:
        return (fct(*args))
    except Exception as e:
        print("Exception: {}".format(e), file = sys.stderr)
        return (None)
