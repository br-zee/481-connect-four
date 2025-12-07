import time

class ConnectFour:

    board = []
    
    _rows = 6
    _cols = 7

    def __init__(self):
        board = []
        for r in range(self._rows):
            board.append([None] * self._cols)

        self.board = board

    def play(self, players):
        from Player import Computer
        
        turn = 0
        self.prettyPrint()

        while (True):

            print(f"{players[turn].name}'s Turn to move")
            
            if isinstance(players[turn], Computer):
                opponent_id = players[1 - turn].id

                t0 = time.perf_counter()
                move = players[turn].choose_move(self, opponent_id)
                t1 = time.perf_counter()
                print(f"Computer chooses column {move + 1}, took {(t1-t0):.2f} seconds")
            
            else:
                print("Pick a column to drop a piece (1-7)")
                print("Valid moves:", self.validMoves())

                try:
                    move = int(input()) - 1

                    # if trying to drop on nonexistent column
                    if move > self._cols - 1:
                        print("Cannot drop there, column is not on board")
                        continue

                    # if trying to drop on column that has no space
                    if move not in self.getValidColumns():
                        continue

                except:
                    print("Invalid move")
                    continue
            
            # drop piece and check if game is over
            rowDropped = self.dropPiece(move, players[turn])
            self.prettyPrint()  

            if self.isGameOver(rowDropped, move, players[turn]):
                print(f"{players[turn].name} wins!")
                break 

            # switch player turns
            turn = 1 if turn == 0 else 0


    def dropPiece(self, col, player):
        rowToDrop = -1 
        for index, row in enumerate(self.board):
            if row[col] == None:
                rowToDrop = index
        
        self.board[rowToDrop][col] = player.id
        return rowToDrop
    
    # creates deeop copy of game state
    def copy(self):
        import copy
        new_game = ConnectFour()
        new_game.board = copy.deepcopy(self.board)
        return new_game

    # simulates a move w/o changing real board
    def simulatedDrop(self, col, player):
        simulated_game = self.copy()

        # find lowest avail. row
        rowToDrop = -1
        for index in range(len(simulated_game.board)):
            if simulated_game.board[index][col] == None:
                rowToDrop = index
        
        # drop the piece
        if rowToDrop != -1:
            simulated_game.board[rowToDrop][col] = player
            return simulated_game, rowToDrop
        return None, None # column is full
    
    # returns list of columns that aren't full
    def getValidColumns(self):
        columns = []
        for col in range(self._cols):
            if self.board[0][col] is None:
                columns.append(col)
        return columns
    
    # [HELPER FUNCTION] check if a specific player has won (used by minimax)
    def checkWinner(self, player_id):
        """check if player_id has 4 in a row anywhere on board"""
        for row in range(self._rows):
            for col in range(self._cols):
                if self.board[row][col] == player_id:
                    # create a mock player object for existing check methods
                    class MockPlayer:
                        def __init__(self, id):
                            self.id = id
                    mock = MockPlayer(player_id)
                    
                    if (self.checkVertical(row, col, mock) >= 4 or
                        self.checkHorizontal(row, col, mock) >= 4 or
                        self.checkDiagonal(row, col, mock) >= 4):
                        return True
        return False


    def validMoves(self):
        moves = []
        for col in range(self._cols):
            for row in range(self._rows - 1, -1, -1):  # move from bottom to top
                if self.board[row][col] is None:
                    moves.append((row, col))
                    break
        return moves
    
    def isGameOver(self, row, col, player):
        v = self.checkVertical(row, col, player) >= 4
        h = self.checkHorizontal(row, col, player) >= 4
        d = self.checkDiagonal(row, col, player) >= 4

        # print("Vertical win?\t", v)
        # print("Horizontal win?\t", h)
        # print("Diagonal win?\t", d)

        return v or h or d

    def checkVertical(self, row, col, player):
        total = 1
        
        bottom = row + 1
        while (bottom < self._rows and self.board[bottom][col] == player.id):
            total += 1
            bottom += 1
        
        return total

    def checkHorizontal(self, row, col, player):
        total = 1
        
        front = col - 1
        while (front >= 0 and self.board[row][front] == player.id):
            total += 1
            front -= 1
        
        back = col + 1
        while (back < self._cols and self.board[row][back] == player.id):
            total += 1
            back += 1

        return total
    
    def checkDiagonal(self, row, col, player):
        total1 = 1
        total2 = 1

        # Check top left
        coords = [row - 1, col - 1]
        while (coords[0] >= 0 and coords[1] >= 0 and self.board[coords[0]][coords[1]] == player.id):
            total1 += 1
            coords[0] -= 1
            coords[1] -= 1

        # Check bottom right
        coords = [row + 1, col + 1]
        while (coords[0] < self._rows and coords[1] < self._cols and self.board[coords[0]][coords[1]] == player.id):
            total1 += 1
            coords[0] += 1
            coords[1] += 1
        
        
        # Check top right
        coords = [row - 1, col + 1]
        while (coords[0] >= 0 and coords[1] < self._cols and self.board[coords[0]][coords[1]] == player.id):
            total2 += 1
            coords[0] -= 1
            coords[1] += 1

        # Check bottom left
        coords = [row + 1, col - 1]
        while (coords[0] < self._rows and coords[1] >= 0 and self.board[coords[0]][coords[1]] == player.id):
            total2 += 1
            coords[0] += 1
            coords[1] -= 1
        
        return total1 if total1 > total2 else total2
    
    def prettyPrint(self):
        print("\n=================================================")
        for col in range(self._cols):
            print(str(col+1).center(7), end="")

        print("\n=================================================")
        for index, row in enumerate(self.board):
            for col in row:

                # emojis are two spaces long 
                printed = "⚫" if col == None else str(col)
                print(printed.center(5), end="|")
            
            print("\n" if index < self._rows else "")
        print("=================================================")


# temporary test for board state utils [will delete]
if __name__ == "__main__":
    game = ConnectFour()
    print("Original board empty?", game.board[5][3] == None)
    
    # Simulate a drop
    sim_game, row = game.simulatedDrop(3, 1)
    
    print("Simulated board has piece?", sim_game.board[row][3] == 1)
    print("Original board still empty?", game.board[5][3] == None)
    print("✅ Test passed!" if game.board[5][3] == None else "❌ Test failed!")