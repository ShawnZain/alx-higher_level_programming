#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    """deletes a value at given index

    Args:
        my_list: list to check for value
        at given index to delete
        idx: index to search for
    """


    if (idx < 0) or (idx >= len(my_list)):
        return my_list

    del my_list[idx]

    return my_list
