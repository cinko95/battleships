import random

def generate_board():
    """Generate an empty board and return it."""
    return [['O' for _ in range(5)] for _ in range(5)]

def place_ships(board, num_ships):
    """Randomly place ships on the board."""
    for _ in range(num_ships):
        ship_row = random.randint(0, 4)
        ship_col = random.randint(0, 4)
        while board[ship_row][ship_col] == 'X':
            ship_row = random.randint(0, 4)
            ship_col = random.randint(0, 4)
        board[ship_row][ship_col] = 'X'
      
def print_board(board):
    print("\n")

    print("   0 1 2 3 4")
    print("   - - - - -")
    for row_index, row in enumerate(board):
        # 0 | X O O O O
        # 1 | O O O O O
        # 2 | O O O O O
        print(str(row_index) + '| ' + ' '.join(row))

    print("\n")

def get_user_guess():
    """Get and validate the user's guess."""
    while True:
        guess_row = input("Guess Row: \n").strip()
        guess_col = input("Guess Column: \n").strip()

        if not guess_row.isdigit() or not guess_col.isdigit():
            print("Please enter a number for row and column.")
            continue

        guess_row, guess_col = int(guess_row), int(guess_col)

        if not (0 <= guess_row < 5) or not (0 <= guess_col < 5):
            print("Please enter valid row and column numbers (0 to 4).")
            continue

        return guess_row, guess_col

def computer_make_guess(board):
    """Generate a random guess for the computer."""
    guess_row = random.randint(0, 4)
    guess_col = random.randint(0, 4)
    return guess_row, guess_col

def check_guess(board, guess_row, guess_col):
    """Check if a guess hits or misses a ship on the board."""
    if board[guess_row][guess_col] == 'X':
        print("Congratulations! You hit a ship.")
        board[guess_row][guess_col] = 'H'  # Mark the hit on the board
        return True
    else:
        print("Sorry, it's a miss.")
        return False

def check_win(board):
    """Check if the game is won by either player or the computer."""
    return all(cell != 'X' for row in board for cell in row)

def main():
    print("Welcome to Battleships game!")
    player_board = generate_board()
    computer_board = generate_board()
    
    
    place_ships(player_board, 5)  # Place 5 ships on the player's board
    
    place_ships(computer_board, 5)  # Place 5 ships on the computer's board

    for turn in range(10):  # Allow the player and computer to make 10 guesses each
        print(f"Turn {turn + 1}")
        
        print("Player's Turn:")
        guess_row, guess_col = get_user_guess()
        if check_guess(computer_board, guess_row, guess_col):
            print_board(computer_board)
            if check_win(computer_board):
                print("Player wins!")
                break
        else:
            print_board(computer_board)

        print("Computer's Turn:")
        guess_row, guess_col = computer_make_guess(player_board)
        if check_guess(player_board, guess_row, guess_col):
            print("Computer's hit at row", guess_row, "and column", guess_col)
            print_board(player_board)
            if check_win(player_board):
                print("Computer wins!")
                break
        else:
            print_board(player_board)

    print("Game over!")

if __name__ == "__main__":
    main()
