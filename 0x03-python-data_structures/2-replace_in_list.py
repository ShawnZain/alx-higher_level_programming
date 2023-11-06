#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    """a function that replaces the value
    of a list at a particular index

    my_list: list that we will iterate
    idx: index where value will be changed
    element: change the value to this
    """
    if (0 > idx) or (idx >= len(my_list)):
        return my_list
    else:
        my_list[idx] = element
        return my_list
