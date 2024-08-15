#!/usr/bin/python3
""" rotate_2d_matrix module
"""


def rotate_2d_matrix(matrix):
    """ rotate a 2d square matrix 90 degrees clockwise.

    note: NxN matrix only.
    For matrix that is not square use this for transposition

    [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

    Args:
        matrix (list[list[int]]): 2d square matrix to rotate
    """
    n = len(matrix)
    # transposes the matrix inplace
    matrix[:] = [[row[i] for row in matrix] for i in range(n)]
    # reverses each row in the transposed matrix
    [matrix[row].reverse() for row in range(n)]
