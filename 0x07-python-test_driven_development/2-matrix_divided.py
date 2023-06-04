#!/usr/bin/python3
'''This module defines a function "matrix_divided"

The matrix_divided function takes a matrix (list of lists) and divide by a
given divider div

'''


def matrix_divided(matrix, div):
    '''Divide matrix by div and return the result
    Args:
        matrix (list of lists): matrix of integer of float
        div (int or float): integer divisor

    Returns:
        new matrix: result of dividing matrix by div
    '''
    row_len = 0
    error_1 = 'matrix must be a matrix (list of lists) of integers/floats'

    if (type(matrix) != list or not matrix or
            not matrix[0] or any(type(row) != list for row in matrix)):
        raise TypeError(error_1)

    row_len = len(matrix[0])

    if any(len(row) != row_len for row in matrix):
        raise TypeError('Each row of the matrix must have the same size')

    if any(any(type(itm) not in (int, float) for itm in row)
            for row in matrix):
        raise TypeError(error_1)
    if type(div) not in (int, float):
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    return [[round(itm/div, 2) for itm in row] for row in matrix]
