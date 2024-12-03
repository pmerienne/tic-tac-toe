# Objective
Develop a Python-based [Tic-Tac-Toe game](https://en.wikipedia.org/wiki/Tic-tac-toe). 
This classic exercise helps solidify foundational programming concepts.

To start this exercise, you'll need to implement the `Game` class in the `tic_tac_toe.app module`. 
This class will form the core logic of the Tic-Tac-Toe game and should fully enforce all game rules.

# Rules
- there are two players in the game (`X` and `O`)
- a game has nine fields in a 3x3 grid
- players take turns taking fields until the game is over
- a player can take a field if not already taken
- a game is over when all fields in a row are taken by a player
- a game is over when all fields in a column are taken by a player
- a game is over when all fields in a diagonal are taken by a player
- a game is over when all fields are taken

# Dev guide
## Setup
```bash
pyenv virtualenv 3.10.7 tic-tac-toe
pyenv local tic-tac-toe
poetry install
```

## How to run
To start the game, execute the `main.py` file and follow the prompts to input player moves. 
Enjoy a classic game of Tic-Tac-Toe right from your terminal!