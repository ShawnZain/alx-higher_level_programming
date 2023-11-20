#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """Does division on each element at the same
    index on 2 lists and returns a new list with the results

    Args:
        my_list_1 (list): list 1
        my_list_2 (list): list2
        list_length: length of the new list

    Return: new list of list_length with the result of
        divisions
    """
    
    new_list = []

    #iterate through your new list to assign division values
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            result = 0
            print("wrong type")
        except ZeroDivisionError:
            result = 0
            print("division by 0")
        except IndexError:
            result = 0
            print("out of range")
        finally:
            new_list.append(result)

    return (new_list)
