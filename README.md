# Number Guessing Game 🎯

A fun and challenging number guessing game with an advanced hint system and scoring mechanics.

## Features ✨

- **3 Difficulty Levels**: Easy (10 attempts), Medium (5 attempts), Hard (3 attempts)
- **11 Different Hint Types**: From basic even/odd to complex mathematical properties
- **Smart Scoring System**:  
  - Base points by difficulty
  - Time bonuses with linear scaling
  - Perfect game bonuses
  - Hint penalty system
- **Professional Code Structure**: Modular design with separate files for different functionalities

## How to Play 🎮

1. Run the game: `python main.py`
2. Choose your difficulty level
3. Guess a number between 1-100
4. Type `H` for hints (costs points!)
5. Try to guess in as few attempts and as little time as possible

## Scoring System 🏆

### Base Points by Difficulty

- **Easy**: 100 points
- **Medium**: 500 points  
- **Hard**: 1000 points

### Bonus Points

- **Unused Attempts**: 10/50/100 points per unused attempt
- **Perfect Game** (1 attempt): 50/150/300 bonus points
- **Speed Bonus**: Up to 90/450/900 points for guessing in ≤10 seconds
- **Time Scaling**: Linear bonus reduction from 10-60 seconds

### Penalties

- **Hints**: 10-50 points depending on hint difficulty

## Hint System 💡

The game offers 11 different types of hints:

- Even/Odd (50 pts penalty)
- Divisibility clues (30 pts penalty)
- Fibonacci sequence (10 pts penalty)
- Digit sum properties (10 pts penalty)
- Range hints (50 pts penalty)
- Prime/Perfect square (10 pts penalty)
- And more!

## Project Structure 📁

- ├── main.py           # Entry point
- ├── game_logic.py     # Core game functions
- ├── scoring.py        # Score calculation system
- ├── hints.py          # Hint system and math helpers
- ├── utils.py          # Input validation utilities
- └── scores.txt        # High score storage

## Requirements 📋

- Python 3.10+ (uses match-case statements)
- No external dependencies required

## Installation & Running 🚀

1. Clone or download the project
2. Navigate to the project directory
3. Run: `python main.py`
4. Enjoy the game!

## Author 👨‍💻

Created as a learning project to practice:

- Function organization and modular programming
- Algorithm implementation (linear scaling, mathematical checks)
- File I/O operations
- Game logic and user interaction

---

*Have fun guessing! 🎉*

[Project URL](https://github.com/erik-manukyan/Number-Guessing-Game)
