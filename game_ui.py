import pygame
import sys
from ConnectFour import ConnectFour
from Player import Player, Computer

# Constants
BLUE = (0, 102, 204)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

SQUARESIZE = 100
RADIUS = int(SQUARESIZE / 2 - 5)

ROWS = 6
COLS = 7

WIDTH = COLS * SQUARESIZE
HEIGHT = (ROWS + 1) * SQUARESIZE  # +1 for top row to show next piece

def draw_board(screen, game):
    """Draw the Connect Four board"""
    # First, fill the screen with black
    screen.fill(BLACK)
    
    for row in range(ROWS):
        for col in range(COLS):
            # Draw blue square with black circle (empty slot)
            # Invert row so row 0 (top of array) appears at bottom of screen
            screen_row = ROWS - 1 - row
            
            pygame.draw.rect(screen, BLUE, 
                           (col * SQUARESIZE, screen_row * SQUARESIZE + SQUARESIZE, 
                            SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, 
                             (int(col * SQUARESIZE + SQUARESIZE/2), 
                              int(screen_row * SQUARESIZE + SQUARESIZE + SQUARESIZE/2)), 
                             RADIUS)
    
    # Draw pieces
    for row in range(ROWS):
        for col in range(COLS):
            if game.board[row][col] == 0:
                color = RED
            elif game.board[row][col] == 1:
                color = YELLOW
            else:
                continue
            
            # Invert row so row 0 (top of array) appears at bottom of screen
            screen_row = ROWS - 1 - row
            
            pygame.draw.circle(screen, color, 
                             (int(col * SQUARESIZE + SQUARESIZE/2), 
                              int(screen_row * SQUARESIZE + SQUARESIZE + SQUARESIZE/2)), 
                             RADIUS)
    
    pygame.display.update()

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Connect Four')
    
    # Create game and players
    game = ConnectFour()
    player1 = Player(0, "Player 1")
    player2 = Computer(1, "AI", difficulty=2)  # Medium difficulty
    players = [player1, player2]
    
    turn = 0
    game_over = False
    font = pygame.font.SysFont("monospace", 75)
    
    draw_board(screen, game)
    
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            if event.type == pygame.MOUSEMOTION and not isinstance(players[turn], Computer):
                pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, SQUARESIZE))
                posx = event.pos[0]
                color = RED if turn == 0 else YELLOW
                pygame.draw.circle(screen, color, (posx, int(SQUARESIZE/2)), RADIUS)
                pygame.display.update()
            
            if event.type == pygame.MOUSEBUTTONDOWN and not isinstance(players[turn], Computer):
                pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, SQUARESIZE))
                
                # Get column from mouse position
                posx = event.pos[0]
                col = int(posx // SQUARESIZE)
                
                if col in game.getValidColumns():
                    row = game.dropPiece(col, players[turn].id)  # Pass .id not the player object
                    draw_board(screen, game)
                    
                    if game.isGameOver(row, col, players[turn]):
                        label = font.render(f"{players[turn].name} wins!", 1, RED if turn == 0 else YELLOW)
                        screen.blit(label, (40, 10))
                        pygame.display.update()
                        pygame.time.wait(3000)
                        game_over = True
                    
                    turn = 1 if turn == 0 else 0
        
        # Computer's turn
        if not game_over and isinstance(players[turn], Computer):
            opponent_id = players[1 - turn].id
            col = players[turn].choose_move(game, opponent_id)
            
            row = game.dropPiece(col, players[turn].id)  # Pass .id not the player object
            draw_board(screen, game)
            
            if game.isGameOver(row, col, players[turn]):
                label = font.render(f"{players[turn].name} wins!", 1, YELLOW)
                screen.blit(label, (40, 10))
                pygame.display.update()
                pygame.time.wait(3000)
                game_over = True
            
            turn = 1 if turn == 0 else 0

if __name__ == "__main__":
    main()