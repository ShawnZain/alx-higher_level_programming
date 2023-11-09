#!/usr/bin/python3


def search_replace(my_list, search, replace):
    """Checks if an element exits in the list
    and replaces it with the given value for
    all instances that it occurs

    Args:
        my_list: list to check in
        search: element to look for in the list
        replace: value to replace it with

    Return the new list, or the old one if there
    is no occurance of the searched value
    """


    if my_list.count(search) == 0:
        return my_list
    else:
        new_list = []

        for value in my_list:
            if value == search:
                new_list.append(replace)
            else:
                new_list.append(value)

    #list comprehension method:
    #if my_list.count(search) != 0:
        #new_list = [item if item != search else replace for item in my_list]
        #return new_list
    #elif my_list.count(search) == 0:
        #return my_list

        return new_list
