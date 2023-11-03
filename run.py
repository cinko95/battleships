board = [['O' for _ in range(6)] for _ in range(6)]

import random

def place_ship(board):
    ship_row = random.randint(0, 5)
    ship_col = random.randint(0, 5)
    board[ship_row][ship_col] = 'S'

def print_board(board):
    for row in board:
        print(' '.join(row))
