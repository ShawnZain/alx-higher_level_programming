#!/usr/bin/python


def multiple_returns(sentence):
    """Returns the length of the statement
    and the first letter of the sentence

    Args:
        sentence: string
    """


    my_tuple = ()

    if not sentence:
        my_tuple = (0, "None")
    else:
        my_tuple = (len(sentence), sentence[0])

    return my_tuple
