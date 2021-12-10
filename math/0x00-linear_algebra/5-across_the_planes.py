#!/usr/bin/env python3
""" Across the planes """


def add_matrices2D(mat1, mat2):
    """
    Function that adds two matrices element-wise
    """
    if len(mat1[0]) != len(mat2[0]):
        return None
    new_matrix = []
    for i in range(len(mat1)):
        temp = []
        for j in range(len(mat1[0])):
            temp.append(mat1[i][j] + mat2[i][j])
        new_matrix.append(temp)
    return new_matrix
