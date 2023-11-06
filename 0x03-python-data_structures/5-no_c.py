#!/usr/bin/python3


def no_c(my_string):
    """a function that takes a string
    and removes all c and C

    my_string: string argument to take
    """
    
    #method 1 with list comprehension
    return''.join(char for char in my_string if char not in "cC")

    """method 2:
    result = ""
    for char in my_string:
        if char not in "cC":
            result += char
    return result
    """
