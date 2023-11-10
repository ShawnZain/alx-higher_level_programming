#!/usr/bin/python3


def best_score(a_dictionary):
    """returns a key with the biggest integer value

    loop through the whole dictionary and check
    if the value is higher than the next saving
    the higher value in a variable max.
    At the end of the loop return max.
    If the dict has no scores return 'None'

    Args:
        a_dictionary: dictionary to check for max
    """


    max_val = 0
    max_key = None

    if a_dictionary == None:
        return None
    else:
        for key, value in a_dictionary.items():
            if value > max_val:
                max_key = key
                max_val = value
        return max_key
