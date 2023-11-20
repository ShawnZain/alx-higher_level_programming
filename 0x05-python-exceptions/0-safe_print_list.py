#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """print x elements of the list

    Args:
        my_list (list): the list to print elements from
        x (int): the number of elements of list to print

    Return:
        The number of elements printed
    """

    count = 0 #Tracks the number of elements printed

    try:
        for i in range(x):
            print(my_list[i], end = "")
            count += 1
    except (IndexError, ValueError, TypeError):
        """IndexError occurs when the list does not have enough elements
        ValueError & TypeError occurs when x is not an int
        """
        pass
    finally:
        print()
    return count
