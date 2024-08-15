#!/usr/bin/python3
""" rotate_2d_matrix module
"""


def rotate_2d_matrix(matrix: list[list[int]]) -> None:
    """ rotate a 2d square matrix 90 degrees clockwise.

    note: NxN matrix only

    Args:
        matrix (list): 2d square matrix to rotate
    """
    n = len(matrix)
    # transposes the matrix inplace
    matrix[:] = [[row[i] for row in matrix] for i in range(n)]
    # reverses each row in the transposed matrix
    [matrix[row].reverse() for row in range(n)]
