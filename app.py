import random

def hangman():
    # List of 5 predefined words
    words = ["python", "github", "coding", "hangman", "computer"]
    
    # Select a random word
    word = random.choice(words).upper()
    word_letters = set(word)
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect = 6
    
    print("Welcome to Hangman!")
    print("You have 6 incorrect guesses allowed.")
    print(f"The word has {len(word)} letters.")
    
    while incorrect_guesses < max_incorrect and word_letters:
        # Display current state
        print(f"\nWord: {' '.join([letter if letter in guessed_letters else '_' for letter in word])}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
        print(f"Incorrect guesses remaining: {max_incorrect - incorrect_guesses}")
        
        # Get user input
        guess = input("Guess a letter: ").upper()
        
        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        # Add guess to guessed letters
        guessed_letters.add(guess)
        
        # Check if guess is correct
        if guess in word_letters:
            word_letters.remove(guess)
            print(f"Good guess! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.")
    
    # Game over - check win/loss
    if word_letters:
        print(f"\nYou lost! The word was: {word}")
    else:
        print(f"\nCongratulations! You guessed the word: {word}")

if __name__ == "__main__":
    while True:
        hangman()
        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break5