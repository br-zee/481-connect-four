from ConnectFour import ConnectFour
from Player import Player, Computer

if __name__ == "__main__":

    connectFour = ConnectFour()

    player1 = Player("🔴", "Player 1")
    player2 = Computer("🟡", "AI")

    players = [player1, player2]
    turn = 0

    connectFour.play(players)

    

