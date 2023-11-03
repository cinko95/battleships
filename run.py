board = [['O' for _ in range(6)] for _ in range(6)]

import random

def place_ship(board):
    ship_row = random.randint(0, 4)
    ship_col = random.randint(0, 4)
    board[ship_row][ship_col] = 'S'