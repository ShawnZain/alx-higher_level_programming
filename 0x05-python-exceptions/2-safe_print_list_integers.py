#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """prints x number of integers from my_list
    my_list can have data of any type
    x has to be an int
    x can be bigger than len(my_list) - raise the IndexError

    All integers have to be printed on the same line followed
    by a new line - other type of value in the list must be
    skipped (in silence).

    Args:
        my_list (list): list where x elements will be printed
        x (int): number of elements to print ut

    Returns:
        Number of elements printed
    """

    counter = 0

    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end = "")
            counter += 1
        except (ValueError, TypeError):
            continue
        except IndexError:
            raise

    print()
    return (counter)
