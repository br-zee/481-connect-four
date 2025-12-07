import random

class Player:

    id = -1
    name = ""

    def __init__(self, id, name):
        self.id = id
        self.name = name


class Computer(Player):

    selected_difficulty = {}
    difficulties = [
        {
           "name": "Easy",
           "depth": 1,
           "random_chance": 0.75
        },
        {
            "name": "Medium",
            "depth": 2,
            "random_chance": 0.45
        },
        {
            "name": "Hard",
            "depth": 4,
            "random_chance": 0.25
        },
        {
            "name": "Impossible",
            "depth": 6,
            "random_chance": 0.00001
        }
    ]

    def __init__(self, id, name="Computer", difficulty = 0):
        super().__init__(id, name)
        self.selected_difficulty = self.difficulties[difficulty]
        self.name = f"{self.selected_difficulty['name']} {name}"
        
    def choose_move(self, game, opponent_id):
        from minimax import minimax
        
        valid_columns = game.getValidColumns()
        best_score = float('-inf')
        best_col = valid_columns[0]

        scores = []
        
        for col in valid_columns:
            row = game.dropPiece(col, self.id) 
            score = minimax(game, self.selected_difficulty["depth"], False, self.id, opponent_id)
            game.undoDrop(row, col)

            # add noise to score randomly
            if random.random() < self.selected_difficulty["random_chance"]:
                score += random.randint(-5, 5)

            if random.random() <= self.selected_difficulty["random_chance"]:
                scores.append([score, col])

            if score > best_score:
                best_score = score
                best_col = col
        
        # randomly choose to select from all possible moves or choose best
        if random.random() < self.selected_difficulty["random_chance"]:
            print(f"AI chose randomly from: {scores}")
            return random.choice(scores)[1] if len(scores) > 0 else best_col
        else:
            return best_col