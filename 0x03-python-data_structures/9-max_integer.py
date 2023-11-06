#!/usr/bin/python3


def max_integer(my_list=[]):
    """returns the largest int in the list

    Args:
        my_list: list to check for
    """


    sorted_list = sorted(my_list)
    return (sorted_list[len(sorted_list) - 1])
