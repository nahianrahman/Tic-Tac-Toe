# Tic-Tac-Toe
A command line based implementation of the classic Tic-Tac-Toe game, with two levels of difficulty

## Files
This project contains 2 files:
1. player.py: This file contains the three player classes and their respective move-selection methods.
2. game.py: This file contains the game board and manages the gameplay.

## Installation
1. Make sure you have Python installed (version 3 or above).
2. Clone or download the repo

## Usage
1. Open the game.py file in your Python environment.
2. Run the script.
3. You will be prompted to select the difficulty level:
  - Type '1' for Easy: Play against a computer player that places its moves randomly.
  - Type '2' for Hard: Play against a computer player that uses the minimax algorithm.
4. The game will start, and you will see the board with numbers indicating the positions of each square.
5. The game will prompt each player to enter their moves. On your turn, enter the number corresponding to the square you want to place your move.
6. The game will continue until there is a winner or a tie.

## Note
The RandomComputerPlayer class selects its moves randomly, so it may not always make optimal moves. On the other hand, the GeniusComputerPlayer class uses the minimax algorithm to make intelligent moves and cannot be defeated.

## License
This project is licensed under the [MIT License](LICENSE).
