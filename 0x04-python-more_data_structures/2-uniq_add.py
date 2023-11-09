#!/usr/bin/python3


def uniq_add(my_list=[]):
    """Gets the sum of the unique
    integers in a list

    Args:
        my_list: list to get the integers
        from
    """


    new_list = set(my_list)
    sum = 0

    for i in new_list:
        sum += i

    return sum

    #sum = (sum + i for i in set(my_list))
