#!/usr/bin/python3


def element_at(my_list, idx):
    """function that retrieves the value at
    a given index

    my_list: list to retrieve value from
    idx: index that we are looking for
    """
    list_len = len(my_list)

    if (idx > list_len) or (idx < 0):
        return None
    else:
        return my_list[idx]
