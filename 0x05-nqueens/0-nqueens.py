#!/usr/bin/env python3
""" N queens problem
"""
# If the user called the program with the wrong number of arguments, print Usage: nqueens N, followed by a new line, and exit with the status 1
# where N must be an integer greater or equal to 4
# If N is not an integer, print N must be a number, followed by a new line, and exit with the status 1
# If N is smaller than 4, print N must be at least 4, followed by a new line, and exit with the status 1
# The program should print every possible solution to the problem
# One solution per line
# Format: see example
# You don’t have to print the solutions in a specific order
# You are only allowed to import the sys module
import sys
if __name__ == '__main__':
    # check arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    n = sys.argv[1]
    if not n.isdigit():
        print("N must be a number")
        exit(1)
    n = int(n)
    if n < 4:
        print("N must be at least 4")
        exit(1)

    # Inintializing 2D board with zeros
    board = [[0 for _ in range(n)] for i in range(n)]
    size = len(board)

    # Initialize solutions with empty list
    Solutions = []

    def print_board(board):
        print('---------------------------------')
        for row in reversed(board):
            print(row)

    def explore_queen(board):
        # scan board for first availabe location
        i, j = get_available_location(board)
        if i and j:
            # starting from that cell, get next possible location and go on
            if good_cell(board, i, j):
                pass

    def get_available_location(board):
        for i in len(board):
            for j in len(board):
                if board[i][j] == 0:
                    return i, j
        return None, None

    def good_cell(board, i, j):
        # check row
        for _ in range(len(board)):
            if _ != i and board[i, _] == 1:
                return False
        # check col
        for _ in range(len(board)):
            if _ != j and board[_, j] == 1:
                return False
        # check diagnoal
        for _ in range(len(board)):
            if board[i, _] == 1:
                return False

    # start with first cell, choose it and try to find solution based on that choice
    # be assign it to the proposed solution and go on to place next queen in first available
    # cell and go on till all board cells are covered or solution is captured

    def place_next_queen(i, j, board_sol):
        pass
        # explore next availabe spot

    def mark_diag(_i, _j, i_inc, j_inc, board_sol):
        while (_i >= 0 and _i < size) and (_j >= 0 and _j < size):
            board_sol[_i][_j] = 1
            _i += i_inc
            _j += j_inc

    def mark_cell(i, j, board_sol):
        if i < 0 or i >= size or j < 0 or j >= size:
            raise (IndexError)
        # mark_row i
        for _ in range(size):
            board_sol[i][_] = 1
        # mark col j
        for _ in range(size):
            board_sol[_][j] = 1
        # mark diagonal
        mark_diag(i, j, 1, 1, board_sol)
        mark_diag(i, j, -1, -1, board_sol)
        mark_diag(i, j, 1, -1, board_sol)
        mark_diag(i, j, -1, 1, board_sol)

    def next_availabe_spot(board_sol):
        for _i in range(size):
            for _j in range(size):
                if not board_sol[_i][_j]:
                    return _i, _j
        return None, None

    def explore_solution_starting_from(i, j):
        # starting from that cell, place the first queen and initiate a propsed solution and go on
        prop_sol = []
        prop_sol.append((i, j))
        board_sol = [[0 for _ in range(n)] for i in range(n)]

        # mark all ver, hor, diag cells
        mark_cell(i, j, board_sol)
        print_board(board_sol)
        # place next queen
        while (True):
            # get next availabe place
            next_i, next_j = next_availabe_spot(board_sol)
            # print(next_i, next_j)
            if next_i is None or next_j is None:
                break
            mark_cell(next_i, next_j, board_sol)
            prop_sol.append((next_i, next_j))
            # print_board(board_sol)
        # count no. of cells
        print('len of solution is ', len(prop_sol))
        if (len(prop_sol) == size):
            return prop_sol
        else:
            return None

    def start(board):
        for i in range(size):
            for j in range(size):
                if (i, j) not in [cell for solution in Solutions for cell in solution]:
                    sol = explore_solution_starting_from(i, j)
                    if sol:
                        Solutions.append(sol)

    start(board)
    print('Solutions----')
    print(Solutions)
