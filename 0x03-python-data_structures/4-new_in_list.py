#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    """a function that makes a copy of given
    list and changs the value at a given index
    of the new list

    my_list: original list to copy
    idx: index value to change
    element: change the value to this
    """
    new_list = my_list.copy()

    if (0 > idx) or (idx >= len(my_list)):
            return my_list
    else:
        new_list[idx] = element
        return new_list
