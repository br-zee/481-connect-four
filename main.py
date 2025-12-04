from ConnectFour import ConnectFour
from Player import Player

if __name__ == "__main__":

    connectFour = ConnectFour()

    player1 = Player(0, "Player 1")
    player2 = Player(1, "Player 2")

    players = [player1, player2]
    turn = 0

    connectFour.play(players)

    

