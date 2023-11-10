#!/usr/bin/python3


def uppercase(str):
    """checks to see in a character
    in the given string is lowercase then converts it to uppercase

    We cannot import any module

    Args:
        str: string to check for
    """


    #loop through the string to check for lowercase letters
    for chars in str:
        if 97 <= ord(chars) <= 122: # lowercase is from 97 to 122
            chars = chr(ord(chars) - 32) #get the uppercase then cast to char

        print("{}".format(chars), end="")

    print()
