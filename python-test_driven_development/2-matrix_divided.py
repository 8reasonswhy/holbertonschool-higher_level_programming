#!/usr/bin/python3
"""
la fonctionqui fait le truc
"""
def matrix_divided(matrix, div):
    """
    la fonction qui fait la division
    """
    if not (isinstance(div, (int, float))):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    if not ( all(isinstance(x, (int, float)) for row in matrix for x in row)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    elif not (all( len(row) == len(matrix[0]) for row in matrix)):
        raise TypeError("Each row of the matrix must have the same size")
    return [[round(x/2,2) for x in row] for row in matrix]
