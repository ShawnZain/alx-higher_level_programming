#!/usr/bin/python3


def simple_delete(a_dictionary, key=""):
    """deletes a key-value pair

    Args:
        a_dictionary: dict to manipulate
        key: key to delete
    """


    if key in a_dictionary:
        del a_dictionary[key]
    
    return a_dictionary

