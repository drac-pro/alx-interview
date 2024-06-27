#!/usr/bin/python3
"""Defines a function pascal_triangle"""


def pascal_triangle(n):
    """returns a list of lists of integers representing the
    Pascal’s triangle of n

    Args:
        n(int): number of rows of the pascals triangle

    Returns: a list of list with the element being each row of the triangle
    """
    if n <= 0:
        return []
    triangle = []
    for i in range(n):  # optimization can be possible
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle
