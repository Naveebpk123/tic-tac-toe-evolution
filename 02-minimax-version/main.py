import os
from minimax import check_win, check_space, find_best_move

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board(board):
    print("\nBoard:")
    for row in board:
        print(f"{'|'.join(row)}")
    print('\n')

def game():
    board = [['_','_','_'],['_','_','_'],['_','_','_']]
    
    while True:
        choice = input("Type '1' to play against AI\nType '2' to play 2 player mode\n")
        if choice in ['1','2']:
            is_ai = False if choice=='2' else True
            break
        print("Invalid input. Please try again")
        
    while True:
        p1_marker = input("Player 1, do you want to be 'X' or 'O'?\n").upper()
        if p1_marker in ['X', 'O']:
            break
        print('Invalid Input. Please choose X or O.')
        
    p2_marker = 'O' if p1_marker == 'X' else 'X'
    if is_ai:
        print(f'Player 2 (AI Computer) is assigned: {p2_marker}')
    else:
        print(f'Player 2, you are {p2_marker}')
    print_board(board)

    players = [('Player 1', p1_marker), ('AI Computer' if is_ai else 'Player 2', p2_marker)]
    turn = 0 
    
    while True:
        current_player_name, current_marker = players[turn]
        print(f"{current_player_name}'s Turn ({current_marker})")
        
        # --- AI AUTOMATIC LOGIC ---
        if is_ai and current_player_name == 'AI Computer':
            print("AI is calculating options...")
            row, col = find_best_move(board, current_marker)
            
        # --- HUMAN INPUT LOGIC ---
        else:
            try:
                row = int(input('Pick a row (1 for top, 2 for middle, 3 for bottom):\n')) - 1
                col = int(input('Pick a column (1 for first, 2 for second, 3 for third):\n')) - 1
                
                if row not in [0, 1, 2] or col not in [0, 1, 2]:
                    print('Invalid coordinates! Numbers must be between 1 and 3.')
                    continue
                if not check_space(board, row, col):
                    print('This space is already filled')
                    continue
            except ValueError:
                print('Invalid Input. Please enter numbers only.')
                continue

        # Execute move and display the results
        board[row][col] = current_marker
        print_board(board)
        
        win = check_win(board)
        if win:
            if win == 'Draw':
                print("It's a Draw!!!!!!!!!!")
            else:
                print(f"{current_player_name} wins!!!!")
            break 
            
        turn = 1 - turn  # Alternates values between index 0 and 1

# Game launcher loop
while True:
    print('\nWelcome to Python Tic Tac Toe !!!!\n')
    start = input("Type anything to start! Type 'q' to quit.\n").lower()
    if start == 'q':
        print("Goodbye!")
        break
    clear_screen()
    game()
    
    play_again = input("Do you want to play again (y/n)?\n").lower()
    if play_again != 'y':
        print("Thanks for playing!")
        break
