#!/usr/bin/python3
""" Island Perimeter """

# visited_grid = []
# perimeter = 0


def get_first_land_square(grid):
    """ returns x, y of first land square"""
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                return row, col


def getNeighbours(grid, row, col):
    """ get list of all neibours"""
    rows_len = len(grid)
    cols_len = len(grid[0])
    dirs = [
        (-1, 0),
        (0, 1),
        (1, 0),
        (0, -1)]
    lst = [(row + dir[0], col + dir[1]) for dir in dirs]

    return lst


def initialized_visited_grid(grid):
    """ Initialize visited grid """
    global visited_grid
    visited_grid = [
        [False for _ in range(len(grid[0]))] for _ in range(len(grid))]


def calulate_parameters(grid, row, col):
    """ calculate parameters """
    global visited_grid, perimeter
    rows_len = len(grid)
    cols_len = len(grid[0])
    # get neighbours
    # mark as visited
    visited_grid[row][col] = True
    neighbours = getNeighbours(grid, row, col)
    for neighbour in neighbours:
        nei_row = neighbour[0]
        nei_col = neighbour[1]
        if nei_row < 0 or nei_row >= rows_len:
            perimeter += 1
            continue
        if nei_col < 0 or nei_col >= cols_len:
            perimeter += 1
            continue

        # if not visited before and holds 1
        if visited_grid[nei_row][nei_col]:
            continue
        if grid[nei_row][nei_col]:
            calulate_parameters(grid, nei_row, nei_col)
        else:
            perimeter += 1


def island_perimeter(grid):
    """
    returns the perimeter of the island described in grid:
    Args:
        @grid: 2D list
    Returns:
        int: perimeter of island
    """
    global perimeter
    perimeter = 0
    # initalize visited squares grid
    initialized_visited_grid(grid)

    # get first land square cordinates
    if not get_first_land_square(grid):
        return 0
    row, col = get_first_land_square(grid)
    # starting from first square
    calulate_parameters(grid, row, col)
    return perimeter
