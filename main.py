from ConnectFour import ConnectFour
from Player import Player, Computer

if __name__ == "__main__":

    connectFour = ConnectFour()

    player1 = Player("🔴", "Player 1")

    print("Select Difficulty:")
    print("(0 - Easy, 1 - Medium, 2 - Hard, 3 - Impossible)")
    difficulty = int(input())

    # player1 = Computer("🔴", "AI 1", difficulty)
    player2 = Computer("🟡", "AI 2", difficulty)

    players = [player1, player2]
    turn = 0

    connectFour.play(players)

    

