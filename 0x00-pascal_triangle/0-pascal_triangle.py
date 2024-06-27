#!/usr/bin/python3
"""Defines a function pascal_triangle"""
from math import comb


def pascal_triangle(n):
    """returns a list of lists of integers representing the
    Pascal’s triangle of n

    Args:
        n(int): number of rows of the pascals triangle

    Returns: a list of list with the element being each row of the triangle
    """
    if n <= 0:
        return []
    triangle = [[1],]
    if n > 1:
        for i in range(1, n):  # optimization can be possible
            row = []
            for j in range(i + 1):
                row.append(comb(i, j))
            triangle.append(row)
    return triangle
