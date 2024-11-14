#!/usr/bin/env python3
""" N queens problem
"""

import sys
from copy import deepcopy
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

    def print_solutions():
        for sol in Solutions:
            print(sol)

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
                    available_spots.append((_i, _j))
        return available_spots

    def explore_solution_starting_from(spot, prop_sol, board_sol):
        # print('Debugging#######################')
        # mark cell
        mark_cell(*spot, board_sol)
        # append to proposed sol
        if spot not in prop_sol:
            prop_sol.append(spot)

        # get remaining available spots
        avai_spots = next_availabe_spots(board_sol)
        # print('len of ava spots', len(avai_spots))

        if not len(avai_spots):
            # check if len of proposed solution == size
            # print('len of solution is ', len(prop_sol))
            if (len(prop_sol) == size) and prop_sol not in Solutions:
                Solutions.append(prop_sol)
            # print_solutions()
            return
        flattened_correct_solutions = [
            cell for sol in Solutions for cell in sol]
        # print(flattened_correct_solutions)
        for spot in avai_spots:
            if spot not in flattened_correct_solutions:
                explore_solution_starting_from(
                    spot, deepcopy(prop_sol), deepcopy(board_sol))

    def start(board):
        for spot in next_availabe_spots(board):
            explore_solution_starting_from(
                spot, [].copy(), deepcopy(board))

    start(board)
    # print('Solutions----')
    print_solutions()
