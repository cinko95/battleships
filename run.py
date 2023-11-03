import random

board = [['O' for _ in range(5)] for _ in range(5)]

def place_ship(board):
    ship_row = random.randint(0, 4)
    ship_col = random.randint(0, 4)
    board[ship_row][ship_col] = 'X'
    print("Battleship placed at row", ship_row, "and column", ship_col)

def print_board(board):
    for row in board:
        print(' '.join(row))

def get_user_guess():
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Column: "))
    return guess_row, guess_col

def check_guess(board, guess_row, guess_col):
    if board[guess_row][guess_col] == 'S':
        print("Congratulations! You hit the ship.")
        return True
    else:
        print("Sorry, it's a miss.")
        return False

# Main game loop
print("Welcome to Battleship game!")
print_board(board)
place_ship(board)

for _ in range(10):  # Allow the player to make 10 guesses
    print("Guess the coordinates:")
    guess_row, guess_col = get_user_guess()
    if check_guess(board, guess_row, guess_col):
        break
    print_board(board)


print_board(board)
print("Game over!")
