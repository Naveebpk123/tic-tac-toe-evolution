import os

def clear_screen():
    # Clears the terminal screen for a cleaner look
    os.system('cls' if os.name == 'nt' else 'clear')

def check_win(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != '_':
            return row[0]
            
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '_':
            return board[0][col]
            
    # Check diagonals
    if board[1][1] != '_':
        if (board[0][0] == board[1][1] == board[2][2]) or (board[0][2] == board[1][1] == board[2][0]):
            return board[1][1]
            
    # Check Draw
    if all(cell != '_' for row in board for cell in row):
        return 'Draw'
        
    return None

# Check if the chosen space is valid and not already occupied
def check_space(board, row, col):
    if board[row][col] != '_':
        print('That space is already filled!')
        return False
    return True

# Function to print the current state of the board in a user-friendly format
def print_board(board):
    print("\nBoard:")
    for row in board:
        print(f"{'|'.join(row)}")
    print('\n')

def game():
    # Initialize the game board as a 3x3 grid filled with underscores to represent empty spaces
    board = [['_','_','_'],['_','_','_'],['_','_','_']]
    
    # Ask Player 1 to choose their marker (X or O) and assign the opposite marker to Player 2. Validate the input to ensure it's either X or O.
    while True:
        p1_marker = input("Player 1, do you want to be 'X' or 'O'?\n").upper()
        if p1_marker in ['X', 'O']:
            break
        print('Invalid Input. Please choose X or O.')
        
    p2_marker = 'O' if p1_marker == 'X' else 'X'
    print(f'Player 2, you are {p2_marker}')
    print_board(board)
    
    # Set up the players
    players = [('Player 1', p1_marker), ('Player 2', p2_marker)]
    turn = 0 
    
    while True:
        current_player_name, current_marker = players[turn]
        print(f"{current_player_name}'s Turn ({current_marker})")
        
        try:
            row = int(input('Pick a row (1 for top, 2 for middle, 3 for bottom):\n')) - 1
            col = int(input('Pick a column (1 for first, 2 for second, 3 for third):\n')) - 1
            
            # Validate the input coordinates to ensure they are within the valid range(1-3 for both row and column) 
            
            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print('Invalid coordinates! Numbers must be between 1 and 3.')
                continue
            # Then check if the chosen space is already occupied before allowing the player to make their move. 
            if not check_space(board, row, col):
                continue
            # Update the board with the current player's marker and print the updated board after each move.    
            board[row][col] = current_marker
            print_board(board)
            
            win = check_win(board)
            if win:
                if win == 'Draw':
                    print("It's a Draw!!!!!!!!!!")
                else:
                    print(f"{current_player_name} wins!!!!")
                break 
                
            turn = 1 - turn  # Switch turns between Player 1 and Player 2 (0 to 1, and 1 to 0)

        # Handle invalid input that cannot be converted to an integer, prompting the user to enter valid numbers for row and column.    
        except ValueError:
            print('Invalid Input. Please enter numbers only.')
            continue

# Main game loop
while True:
    print('\nWelcome to Python Tic Tac Toe!!!!\n')
    start = input("Type anything to start! Type 'q' to quit.\n").lower()
    if start == 'q':
        print("Goodbye!")
        break
    clear_screen()
    game()
    # After the game ends, ask the players if they want to play again. If they choose 'y', the game restarts; otherwise, it exits.
    play_again = input("Do you want to play again (y/n)?\n").lower()
    if play_again != 'y':
        print("Thanks for playing!")
        break