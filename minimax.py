def evaluate_window(window, ai_id, opponent_id):
    """
    evaluating potential (how close a position is to winning/losing) of one specific 4-space pattern
    
    PARAMETERS:
    - window: list of 4 values [player_id, player_id, None, None, etc.]
    - ai_id: The AI's player ID (0 or 1)
    - opponent_id: The opponent's player ID (1 or 0)
    
    SCORING LOGIC:
    - 4 AI pieces = WIN = +100
    - 3 AI pieces + 1 empty = One move from winning = +5
    - 2 AI pieces + 2 empty = Building potential = +2
    
    - 4 opponent pieces = LOSS = -100
    - 3 opponent pieces + 1 empty = Must block! = -4
    
    WHY these scores?
    - We prioritize winning (+5) slightly over blocking (-4) to be aggressive
    - Building 2-in-a-row creates future opportunities
    - Terminal states (4-in-a-row) have highest magnitude
    """
    score = 0
    
    # count how many pieces each player has in this window
    ai_count = window.count(ai_id)
    opponent_count = window.count(opponent_id)
    empty_count = window.count(None)
    
    # score AI's pieces in this window
    if ai_count == 4:
        score += 100  # winning move
    elif ai_count == 3 and empty_count == 1:
        score += 5    # one move away from winning
    elif ai_count == 2 and empty_count == 2:
        score += 2    # building potential
    
    # score opponent's pieces (negative = bad for AI)
    if opponent_count == 4:
        score -= 100  # opponent wings
    elif opponent_count == 3 and empty_count == 1:
        score -= 4    # must block
    
    return score


def evaluate_board(board, ai_id, opponent_id):
    """
    scoring the entire board where the output is the total score for entire board
    (indicating how favorable the position is for the AI)
    
    SCORES:
    positive score = good for AI
    negative score = good for opponent
    zero = neutral position
    
    STRATEGY:
    1. give bonus for controlling center column (more winning paths)
    2. check all possible 4-in-a-row windows:
       - Horizontal (rows)
       - Vertical (columns)  
       - Diagonal (both directions: / and \)
    3. sum up all the scores
    
    PARAMETERS:
    - board: 2D list representing the game board
    - ai_id: AI's player ID
    - opponent_id: Opponent's player ID
    """
    score = 0
    rows = len(board)
    cols = len(board[0])
    
    # center column control
    center_col = cols // 2  # column 3 (middle of 0-6)
    center_array = [board[row][center_col] for row in range(rows)]
    center_count = center_array.count(ai_id)
    score += center_count * 3  # +3 bonus per piece in center
    
    # check horizonal windows
    for row in range(rows):
        for col in range(cols - 3):  # -3 because we need room for 4 spaces
            window = [board[row][col + i] for i in range(4)]
            score += evaluate_window(window, ai_id, opponent_id)
    
    # check verticle windows
    for col in range(cols):
        for row in range(rows - 3):  # -3 because we need room for 4 spaces
            window = [board[row + i][col] for i in range(4)]
            score += evaluate_window(window, ai_id, opponent_id)
    
    # check positive slope diagonals
    for row in range(rows - 3):
        for col in range(cols - 3):
            window = [board[row + i][col + i] for i in range(4)]
            score += evaluate_window(window, ai_id, opponent_id)
    
    # check negative slope diagonals
    for row in range(3, rows):  # start from row 3 and go down
        for col in range(cols - 3):
            window = [board[row - i][col + i] for i in range(4)]
            score += evaluate_window(window, ai_id, opponent_id)
    
    return score


def minimax(game, depth, is_maximizing, ai_id, opponent_id):
    """
    minimax algorithm with recursion to find best move
    """

    # base case 1: we've looked far enough ahead
    if depth == 0:
        return evaluate_board(game.board, ai_id, opponent_id)
    
    # base case 2: ai wins
    if game.checkWinner(ai_id):
        return 10000
    
    # base case 3: opponent wins
    if game.checkWinner(opponent_id):
        return -10000
    
    # base case 4: board is full (tied game)
    valid_columns = game.getValidColumns()
    if len(valid_columns) == 0:
        return 0

    # try all possible moves and pick best one
    if is_maximizing:
        # maximize score for ai
        best_score = float('-inf')
        
        for col in valid_columns:
            result = game.simulatedDrop(col, ai_id)
            sim_game = result[0]
            row = result[1]
            
            if sim_game:
                score = minimax(sim_game, depth - 1, False, ai_id, opponent_id)
                best_score = max(best_score, score)
        
        return best_score
    
    else:
        # minimize score for opponent
        best_score = float('inf')
        
        for col in valid_columns:
            result = game.simulatedDrop(col, opponent_id)
            sim_game = result[0]
            row = result[1]
            
            if sim_game:
                score = minimax(sim_game, depth - 1, True, ai_id, opponent_id)
                best_score = min(best_score, score)
        
        return best_score