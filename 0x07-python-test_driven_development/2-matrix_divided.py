#!/usr/bin/python3

"""Division function"""


def matrix_divided(matrix, div):
    """given a list of lists, divide each
    element of the list with div and create a new
    matrix with the result
    """

    err_msg - "matrix must be a matrix (list of lists) of integers/floats"
    counter = 0

    """test if matrix is a list"""
    if not type(matrix) == list:
        raise TypeError(err_msg)
    
    """test if each row is a list and each element in the matrix is int/ float"""
    if not all(isinstance(row, list) and all(isinstance(element, (int, float))
        for element in row) for row in matrix):
        raise TypeError(err_msg)

    """Test for length of the rows to be the same"""
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError('Each row of the matrix must have the same size')

    """Chcek if div is an int or float"""
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    
    """Check if div is 0"""
    if div == 0:
        raise ZeroDivisionError('division by zero')

    """All checks pass, create new matrix of the given matrix / div"""
    new_matrix = [[round(element / div, 2) for element in row] for row in matrix]

    return new_matrix
