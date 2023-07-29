# Hangman Game

Welcome to our Hangman game built in Python. This game is implemented using pygame and is a simple, but entertaining game of Hangman where the player must guess the word by guessing individual letters within a set number of attempts.

## Table of contents

- [Installation](#installation)
- [Dependencies](#dependencies)
- [How to play](#how-to-play)
- [Project Structure](#project-structure)
- [License](#license)

## Installation

**Step 1:** Clone this repository:

```bash
git clone https://github.com/KnotEnvy/KnotzWordGuess
```

**Step 2:** Navigate to the downloaded folder:

```bash
cd KnotzWordGuess/PygameHangman or cd KnotzWordGuess/TerminalHangman
```

**Step 3:** Run the game:

```bash
python3 game.py or python game.py    for terminal play  python3 main.py or python main.py
```

## Dependencies

This game depends on pygame, a set of Python modules designed for writing video games. To install it, use the following command:

```bash
pip install pygame
```

## How to play

Once the game starts, you will be prompted to choose a difficulty level. Once selected, a random word is chosen from the word bank corresponding to your chosen difficulty level. Your objective is to guess this word.

For each round, you can guess one letter at a time. If your guess is in the word, the letter gets filled in the blank spaces. If it is not, your number of attempts decreases. 

The game continues until you've either guessed the word or you've used up all your attempts. At the end of the game, you have the option to restart and play again.

## Project Structure

The project is split into several files for better organization:

- `Game.py`: This is the main file of the game where everything is put together. It initializes and controls the game flow.

- `Screen.py`: Handles all the visual elements of the game - the display of the start screen, game screen, end screen, as well as displaying messages to the player.

- `WordBank.py`: Contains a set of words to guess from, separated by difficulty levels. It's also responsible for choosing a new random word each round, checking if the guessed letter is in the word, and keeping track of which letters have been guessed.

- `Player.py`: Represents the player. Keeps track of the player's wrong guesses.

## License

This project is licensed under the terms of the MIT license. For more information, see the [LICENSE](LICENSE.md) file.
