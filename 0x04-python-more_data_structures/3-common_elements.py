#!/usr/bin/python3


def common_elements(set_1, set_2):
    """returns a set with values
    common in both the given sets

    Args:
        set_1: first set to compare
        set_2: second set to compare
    """


    common_set = set(set_1 & set_2)

    return common_set
