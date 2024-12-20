#!/usr/bin/python3
""" Island Perimeter """


def island_perimeter(grid):
    """
    returns the perimeter of the island described in grid:
    Args:
        @grid: 2D list
    Returns:
        int: perimeter of island
    """
    # scan row by row from left to right till 1 is found
    sum = 0
    for row in grid:
        for col in row:
            if col == 1:
                sum += 1
                break
    # scan row by row from right to left till 1 is found
    for row in grid:
        for col in reversed(row):
            if col == 1:
                sum += 1
                break

    # Now scan cols, top to botom
    # Now scan cols, top to bottom
    for col in range(len(grid[0])):
        for row in grid:
            if row[col] == 1:
                sum += 1
                break

    # Now scan cols, bottom to top
    for col in range(len(grid[0])):
        for row in reversed(grid):
            if row[col] == 1:
                sum += 1
                break

    return sum
