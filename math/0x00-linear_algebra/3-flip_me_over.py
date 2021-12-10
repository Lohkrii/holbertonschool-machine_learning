#!/usr/bin/env python3
""" Flip me over """


def matrix_transpose(matrix):
    """
    Function that returns the transpose of a matrix:
    """
    matrix_result = [[0 for i in matrix] for j in matrix[0]]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix_result[j][i] = matrix[i][j]
    return matrix_result
