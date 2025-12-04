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
        turn = 0
        self.prettyPrint()

        while (True):

            print(f"{players[turn].name}'s Turn to move")
            print("Pick a column to drop a piece (1-7)")

            print("Valid moves:", self.validMoves())

            try:
                move = int(input()) - 1
                if self.dropPiece(move, players[turn]):
                    break

                turn = 1 if turn == 0 else 0
            
            except:
                print("Invalid move")

    def dropPiece(self, col, player):
        if col > self._cols - 1:
            print("Cannot drop there, column is not on board")
            return False

        rowToDrop = -1 
        for index, row in enumerate(self.board):
            if row[col] == None:
                rowToDrop = index
        
        if rowToDrop != -1:
            self.board[rowToDrop][col] = player.id
            self.prettyPrint()

            if self.isGameOver(rowToDrop, col, player):
                print(f"{player.name} wins!")
                return True
        else:
            print("Cannot drop there, column is full")
            return False       
    
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
            simulated_game.board[rowToDrop][col] = player_id
            return simulated_game, rowToDrop
        return None, None # column is full
    
    # returns list of columns that aren't full
    def getValidColumns(self):
        columns = []
        for col in range(self._cols):
            if self.board[0][col] is None:
                columns.append(col)
        return columns


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
        print("\n===============================================")
        for index, row in enumerate(self.board):
            for col in row:
                printed = "-" if col == None else str(col)
                print(printed.center(7), end="")
            
            print("\n" if index < self._rows else "")
        print("===============================================")
