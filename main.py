from ConnectFour import ConnectFour
from Player import Player, Computer

if __name__ == "__main__":

    connectFour = ConnectFour()

    player1 = Player(0, "Player 1")
    player2 = Computer(1, "AI")

    players = [player1, player2]
    turn = 0

    connectFour.play(players)

    

