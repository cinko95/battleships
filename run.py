board = [['O' for _ in range(6)] for _ in range(6)]

import random

def place_ship(board):
    ship_row = random.randint(0, 5)
    ship_column = random.randint(0, 5)
    board[ship_row][ship_column] = 'S'

def print_board(board):
    for row in board:
        print(' '.join(row))

def get_user_guess():
    guess_row = int(input("Guess Row: "))
    guess_column = int(input("Guess Column: "))
    return guess_row, guess_column

def check_guess(board, guess_row, guess_column):
    if board[guess_row][guess_column] == 'S':
        return True
    return False