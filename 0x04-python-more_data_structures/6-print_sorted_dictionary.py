#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    """Return the value of the sorted dict
    by keys

    Args:
        a_dictionary: the dictionary to sort
    """


    for key, value in sorted(a_dictionary.items()):
        print("{}: {}".format(key, value))
