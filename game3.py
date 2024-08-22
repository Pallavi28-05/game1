import random

def hangman():
    words = ['python', 'hangman', 'challenge', 'programming', 'developer']
    word = random.choice(words)
    word_guessed = ['_'] * len(word)
    attempts = 6
    guessed_letters = []

    print("Welcome to Hangman!")

    while attempts > 0 and ''.join(word_guessed) != word:
        print(f"\nWord: {' '.join(word_guessed)}")
        print(f"Attempts remaining: {attempts}")
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    word_guessed[i] = guess
        else:
            attempts -= 1
            print(f"Incorrect! The letter '{guess}' is not in the word.")

    if ''.join(word_guessed) == word:
        print(f"\nCongratulations! You guessed the word: {word}")
    else:
        print(f"\nGame over! The word was: {word}")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        hangman()

# Start the game
hangman()
