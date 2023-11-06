#!/usr/bin/python3


def element_at(my_list, idx):
    """function that retrieves the value at
    a given index

    my_list: list to retrieve value from
    idx: index that we are looking for
    """
    if (0 > idx) or (idx >= len(my_list)):
        return None
    else:
        return my_list[idx]
