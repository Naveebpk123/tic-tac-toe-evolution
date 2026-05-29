import math

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

def check_space(board, row, col):
    if board[row][col] != '_':
        return False
    return True

def find_best_move(board, ai_marker):
    player_marker = 'X' if ai_marker == 'O' else 'O' # Set markers
    best_score = -math.inf # Set tracking variable to compare and select best score
    best_move = (-1, -1)
    for r in range(3):
        for c in range(3):
            if check_space(board, r, c):
                board[r][c] = ai_marker
                score = minimax(board, 0, False, ai_marker, player_marker)
                board[r][c] = '_'
                # Select the greatest score
                if score > best_score:
                    best_score = score
                    best_move = (r, c)
    return best_move # Return the move which gave highest score after loop ends

def minimax(board, depth, is_maximizing, ai_marker, player_marker):
    result = check_win(board)
    if result == ai_marker:
        return 10 - depth
    elif result == player_marker:
        return depth - 10
    elif result == 'Draw':
        return 0
        
    if is_maximizing:
        max_eval = -math.inf
        for r in range(3):
            for c in range(3):
                if check_space(board, r, c):
                    board[r][c] = ai_marker
                    score = minimax(board, depth + 1, False, ai_marker, player_marker)
                    board[r][c] = '_'  
                    max_eval = max(max_eval, score)
        return max_eval
    else:
        min_eval = math.inf 
        for r in range(3):
            for c in range(3):
                if check_space(board, r, c):
                    board[r][c] = player_marker
                    score = minimax(board, depth + 1, True, ai_marker, player_marker) 
                    board[r][c] = '_' 
                    min_eval = min(min_eval, score) 
        return min_eval