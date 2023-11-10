#!/usr/bin/python3


def islower(c):
    """is lower checks if a char
    provided is lowercase or note
    
    Use the ord() function to get the
    ASCII value of the char given.

    Args:
        c: char to check if lowercase

    Return:
        'True' if lowercase
        'Fasle' if not
    """


    if 97 <= ord(c) <= 122:
        return True
    elif ord(c) < 97 or ord(c) > 122:
        return False
