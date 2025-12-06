class Player:

    id = -1
    name = ""

    def __init__(self, id, name):
        self.id = id
        self.name = name


class Computer(Player):

    def __init__(self, id, name="Computer"):
        super().__init__(id, name)
        
    def choose_move(self, game, opponent_id):
        from minimax import minimax
        
        valid_columns = game.getValidColumns()
        best_score = float('-inf')
        best_col = valid_columns[0]
        
        for col in valid_columns:
            sim_game, row = game.simulatedDrop(col, self.id)
            
            if sim_game:
                score = minimax(sim_game, 4, False, self.id, opponent_id)
                
                if score > best_score:
                    best_score = score
                    best_col = col
        
        return best_col