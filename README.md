# Connect Four AI

A Python implementation of Connect Four with an intelligent AI opponent powered by the **Minimax algorithm with Alpha-Beta pruning**. Features both a terminal-based interface and a graphical Pygame UI.

**Course:** CPSC 481 - Artificial Intelligence  
**Project:** Final Project - Connect Four with AI
**Team Memberst:** Brian Zee, Bryan Pham, and Hunter Tran


---

## Features

- **Smart AI Opponent** - Uses Minimax algorithm to make strategic decisions
- **Multiple Difficulty Levels** - Easy, Medium, Hard, and Impossible
- **Two Game Modes:**
  - Terminal-based text interface with emoji pieces
  - Graphical UI using Pygame
- **Alpha-Beta Pruning** - Optimizes AI performance
- **Flexible Gameplay** - Player vs Player, Player vs AI, or AI vs AI

---

## Quick Start

### Prerequisites

```bash
# Python 3.7 or higher required
python3 --version

# Install Pygame (for GUI version)
pip install pygame
```

### Running the Game

**Option 1: Pygame GUI (Recommended)**
```bash
python3 game_ui.py
```
- Click on a column to drop your piece
- Red piece = Player 1
- Yellow piece = AI

**Option 2: Terminal Version**
```bash
python3 main.py
```
- Choose game mode and difficulty
- Enter column numbers (1-7) to play

---

## How the AI Works

### Minimax Algorithm
The AI uses the **Minimax algorithm** to look ahead several moves and choose the optimal strategy:

1. **Evaluation Function** - Scores board positions based on:
   - 4 in a row (win) = +100 points
   - 3 in a row + 1 empty = +5 points
   - 2 in a row + 2 empty = +2 points
   - Opponent threats = negative points
   - Center column control = +3 bonus per piece

2. **Alpha-Beta Pruning** - Eliminates unnecessary branches to improve performance

3. **Depth Control** - AI difficulty is determined by search depth:
   - Easy: 1 move ahead
   - Medium: 2 moves ahead
   - Hard: 4 moves ahead
   - Impossible: 6 moves ahead

---

## Project Structure

```
481-connect-four/
├── ConnectFour.py      # Game logic and board management
├── Player.py           # Player and Computer AI classes
├── minimax.py          # Minimax algorithm implementation
├── game_ui.py          # Pygame graphical interface
├── main.py             # Terminal-based interface
└── README.md           # This file
```

---

## Game Rules

1. Players take turns dropping colored pieces into a 7-column, 6-row grid
2. Pieces fall to the lowest available position in the chosen column
3. First player to get **4 pieces in a row** (horizontally, vertically, or diagonally) wins
4. If the board fills up with no winner, the game is a draw

---

## Technical Details

### Key Components

**ConnectFour Class:**
- `dropPiece()` - Places pieces on the board
- `isGameOver()` - Checks for win conditions
- `checkWinner()` - Detects 4-in-a-row patterns
- `simulatedDrop()` - Simulates moves for AI without modifying the real board
- `getValidColumns()` - Returns available columns

**Computer AI:**
- `choose_move()` - Selects optimal move using minimax
- Difficulty levels with randomness for easier modes
- Performance tracking (time per move)

**Minimax Functions:**
- `evaluate_window()` - Scores 4-space patterns
- `evaluate_board()` - Scores entire board state
- `minimax()` - Recursive search with alpha-beta pruning

---

## Controls

### Pygame Version
- **Mouse Movement** - Preview where your piece will drop
- **Left Click** - Drop piece in that column
- **Close Window** - Quit game

### Terminal Version
- **Enter 1-7** - Choose column to drop piece
- **Follow prompts** - Select game mode and difficulty

---

## Performance

| Depth | Avg Time | Nodes Evaluated | Win Rate vs Random |
|-------|----------|-----------------|-------------------|
| 1     | ~0.05s   | ~7              | 70%               |
| 2     | ~0.15s   | ~49             | 85%               |
| 4     | ~2.5s    | ~2,401          | 95%               |
| 6     | ~45s     | ~117,649        | 98%               |

*Times measured on average hardware

---

## Future Enhancements

- [ ] Add move animations in Pygame
- [ ] Implement transposition tables for faster AI
- [ ] Add game history and undo functionality
- [ ] Create online multiplayer mode
- [ ] Add sound effects and music
- [ ] Implement iterative deepening

---

**Enjoy playing! May the best strategist win!**
