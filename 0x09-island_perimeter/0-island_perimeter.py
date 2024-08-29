#!/usr/bin/python3
"""Defines a function island_perimeter"""


def island_perimeter(grid):
    """returns the perimeter of the island described in grid
    Args:
        grid(list): list of integers
    Returns:
        perimeter(int): perimeter of the island
    """
    size = 0
    edges = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                size += 1
                if row > 0 and grid[row-1][col] == 1:
                    edges += 1
                if col > 0 and grid[row][col-1] == 1:
                    edges += 1

    return size * 4 - edges * 2
