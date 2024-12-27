# README

## Tic Tac Toe Game

### Description
The Tic Tac Toe game is a graphical implementation of the classic two-player game using Python's Tkinter library. Players take turns marking cells on a 3x3 grid, aiming to form a row, column, or diagonal of their symbol to win.

### Features
- **Two-player gameplay** with customizable symbols and colors.
- Interactive GUI built with Tkinter.
- Tracks player turns and checks for wins or ties.
- Option to reset the game and play again.

### Requirements
- Python 3.6+
- Tkinter (comes pre-installed with Python)

### How to Run
1. Ensure Python is installed on your system.
2. Save the Tic Tac Toe code in a file named `tictactoe.py`.
3. Run the file using the command:
   ```bash
   python tictactoe.py
   ```
4. Play the game by clicking the grid cells.

### Game Controls
- **Player Moves**: Click on an empty cell to place your symbol.
- **Menu**: Use the "File" menu to reset the board or exit the game.

---

## Hangman Game

### Description
The Word Guessing Game is a console-based hangman-style game where the player guesses a word by proposing letters within a limited number of attempts.

### Features
- Word selection from a predefined list.
- Tracks guessed letters and remaining attempts.
- Provides visual feedback for correct and incorrect guesses.
- Dynamic word reveal as correct letters are guessed.

### Requirements
- Python 3.6+

### How to Run
1. Save the Word Guessing Game code in a file named `word_guessing_game.py`.
2. Run the file using the command:
   ```bash
   python word_guessing_game.py
   ```
3. Follow the prompts to play the game.

### Gameplay Instructions
1. The game randomly selects a word from a predefined list.
2. Guess letters one at a time.
   - Correct guesses reveal the letter's position(s) in the word.
   - Incorrect guesses reduce the remaining attempts.
3. Win by guessing the entire word before running out of attempts.

### Customization
- Modify the `word_list` variable to add or change the available words.
- Adjust the `max_attempts` variable to change the difficulty level.
