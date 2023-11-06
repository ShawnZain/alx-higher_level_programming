#!/usr/bin/python3

def print_list_integer(myList=[]):
    """a function that prints the integers
    in the list provided as argument:

    myList: the list whose integers we print
    """
    for i in range(len(myList)):
        print(myList[i])
