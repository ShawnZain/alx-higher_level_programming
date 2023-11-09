#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """takes in a 2D list
    returns a list of the squares of the
    list

    2D list - loop through the inner list, then the outer

    Args:
        matrix: a 2D list
    """

    #using list comprehension
    squared_matrix = [[x * x for x in row] for row in matrix]

    #using lambda
    #squared_matrix = list(map(lambda row: list(map(lambda x: x * x, row)), matrix))

    return squared_matrix
