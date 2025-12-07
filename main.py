from ConnectFour import ConnectFour
from Player import Player, Computer

if __name__ == "__main__":

    connectFour = ConnectFour()

    print("Pick a gamemode (Enter 0-2)")
    print("0 - Player v Player,\n1 - Player v AI,\n2 - AI v AI")
    gamemode = int(input())

    difficulty = None
    if gamemode != 0:
        print(f"\nSelect Difficulty for AI 1")
        print("0 - Easy,\n1 - Medium,\n2 - Hard,\n3 - Impossible")
        difficulty = int(input())

    player1 = Player("🔴", "Player 1") if gamemode != 2 else Computer("🔴", "AI 1", difficulty)

    difficulty2 = None
    if gamemode == 2:
        print(f"\nSelect Difficulty for AI 2")
        print("0 - Easy,\n1 - Medium,\n2 - Hard,\n3 - Impossible")
        difficulty2 = int(input())

    player2 = Player("🟡", "Player 2") if gamemode == 0 else Computer("🟡", "AI 2", difficulty2 if difficulty2 != None else difficulty)

    players = [player1, player2]
    turn = 0

    connectFour.play(players)

    

