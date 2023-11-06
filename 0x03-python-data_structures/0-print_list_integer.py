#!/usr/bin/python3


def print_list_integer(my_list=[]):
    """a function that prints the integers
    in the list provided as argument:

    myList: the list whose integers we print
    """
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))
