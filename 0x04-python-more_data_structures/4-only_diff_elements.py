#!/usr/bin/python 3


def only_diff_elements(set_1, set_2):
    """a function that gets values that are
    not shared by the 2 sets

    Args:
        set_1: first set to compare
        set_2: second set to cmpare
    """


    unique_set = set(set_1 ^ set_2)

    return unique_set
