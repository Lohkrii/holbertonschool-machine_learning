#!/usr/bin/env python3
"""returns the shape of a matrix"""

def matrix_shape(matrix):
    """
    Returns the shape of a matrix.
    """
    shape = [len(matrix)]

    while type(matrix) == list:
        if type(matrix[0]) == list:
            shape.append(len(matrix[0]))
            matrix = matrix[0]
        else:
            matrix = matrix[0]
    return shape
