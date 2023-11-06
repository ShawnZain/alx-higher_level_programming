#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    """a function that will take a list
    reverse it and print each value of the
    list as integer in a new line

    my_list: the input list
    """
    my_list.reverse()
    list_len = len(my_list)

    for i in range(list_len):
        print("{:d}".format(my_list[i]))
