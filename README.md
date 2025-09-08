# Hangman Game

A simple text-based Hangman game implemented in Python where players guess a word one letter at a time.

## Features

- 5 predefined words for guessing
- 6 incorrect guesses allowed
- Input validation for single letters only
- Prevents duplicate guesses
- Play again option
- Clean console interface

## How to Play

1. Run the game
2. A random word is selected from the predefined list
3. Guess letters one at a time
4. You win if you guess all letters before making 6 incorrect guesses
5. You lose if you make 6 incorrect guesses

## Installation

1. Clone this repository:
```bash
git clone https://github.com/Deepu5635/Hungman Game.git
```

2. Navigate to the project directory:
```bash
cd hangman-game
```

3. Run the game:
```bash
python app.py
```

## Requirements

- Python 3.x
- No external dependencies required

## Game Rules

- Enter one letter at a time
- Case doesn't matter (all input is converted to uppercase)
- You have 6 incorrect guesses before losing
- Duplicate guesses are not counted against you
- Words are selected randomly from: PYTHON, GITHUB, CODING, HANGMAN, COMPUTER

## Example Gameplay

```
Welcome to Hangman!
You have 6 incorrect guesses allowed.
The word has 6 letters.

Word: _ _ _ _ _ _
Guessed letters: 
Incorrect guesses remaining: 6
Guess a letter: p

Good guess! 'P' is in the word.

Word: P _ _ _ _ _
Guessed letters: P
Incorrect guesses remaining: 6
Guess a letter: y

Good guess! 'Y' is in the word.
...
```

## Contributing

Feel free to fork this project and submit pull requests for any improvements!

## License

This project is open source and available under the MIT License.
