#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    """provided an input list
    print out the list ina matrix of integers
    The matrix will basically be same as the list
    but with no deliminators apart from space
    and at the end of the column, we append $

    matrix[[]]: the list to convert to matrix
    """

    if matrix is None:
        print("\n")
        return

    for row in matrix:
        for j, val in enumerate(row):
            if j < len(row) - 1:
                print("{:d}".format(val), end = " ")
            else:
                print("{:d}".format(val))
