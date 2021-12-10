#!/usr/bin/env python3
""" Gettin Cozy """


def cat_matrices2D(mat1, mat2, axis=0):
    """
    Function that concatenates two matrices along a specific axis.
    """
    if len(mat1[0]) == len(mat2[0]) and axis == 0 :
        return mat1 + mat2
    elif axis == 1 and len(mat1) == len(mat2):
        matrix = []
        for i in range(len(mat1)):
            matrix.append(mat1[i] + mat2[i])
        return (matrix)
    else:
        return (None)