#!/usr/bin/python


def multiple_returns(sentence):
    """Returns the length of the statement
    and the first letter of the sentence

    Args:
        sentence: string
    """


    if not sentence:
        return (0, None)

    return (len(sentence), sentence[0])
