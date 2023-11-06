#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    """checks if the items in a list are
    divisible by 2 an sets the value of
    a new list to 'True' or 'False'
    at the same index as the list given

    Args:
        my_list: list to check if
        values are divisble by 2
    """


    new_list = [x % 2 == 0 for x in my_list]

    return new_list
