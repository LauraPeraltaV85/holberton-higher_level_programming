#!/usr/bin/python3
"""
   Divide elements of a matrix
"""
def matrix_divided(matrix, div):
    """ Matrix divided, returns a new matrix.
    takes a matrix that must be a list of lists
    of integers/floats and a divisor
    """
    new_matrix = [[]]
    x = 0
    y = 0
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len(matrix[0]) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(matrix[x][y], (int, float)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    elif not all(len(x) == len(matrix[0]) for x in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    elif not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return new_matrix
