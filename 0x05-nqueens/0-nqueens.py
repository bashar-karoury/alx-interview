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

    def next_availabe_spots(board_sol):
        available_spots = []
        for _i in range(size):
            for _j in range(size):
                if not board_sol[_i][_j]:
                    available_spots.append(_i, _j)
        return available_spots

    def explore_solution_starting_from(prop_sol, board_sol):
        # get remaining available spots
        avai_spots = next_availabe_spots(board_sol)
        if not len(avai_spots):
            # check if len of proposed solution == size
            print('len of solution is ', len(prop_sol))
            if (len(prop_sol) == size):
                Solutions.append(prop_sol)

        for spot in avai_spots:
            # mark cell
            mark_cell(*spot, board_sol)
            # append to proposed sol
            prop_sol.append(spot)
            explore_solution_starting_from(*spot)

    def start(board):
        explore_solution_starting_from([], board)
    start(board)
    print('Solutions----')
    print(Solutions)
