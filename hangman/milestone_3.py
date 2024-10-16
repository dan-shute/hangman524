# This file is for the milestone 3 section of the Hangman Project.
# Import modules
import random

# Create a function called check_guess that checks if the letter is in the word.
def check_guess(guess):
    guess = guess.lower()

    # Check if the letter is in the random word.
    if guess in word:
        print(f'Good guess! {guess} is in the word.')
        for index, letter in enumerate(word):
            if letter == guess:
                word_guessed[index] = guess
                print(word_guessed)
    else:
        print(f'Sorry, {guess} is not in the word. Try again.')

# Create a function called ask_for_input that will get the user's guess, check if it is a valid guess and call check_guess.
def ask_for_input():
    # Create a while loop that asks a user for an input, check if the input is valid.
    while True:
        # Get the user input
        guess = input('Please enter a single letter guess: ')

        # Check if the input meets the valid criteria
        if len(guess) == 1 and guess.isalpha() == True:
            break
        else:
            print('Invalid letter. Please, enter a single alphabetical character.')
    
    check_guess(guess)

# Create the fruit list
word_list = ['passionfruit', 'strawberry', 'apple', 'banana', 'mango']

# Use the random module to choice a word from the list at random.
word = random.choice(word_list)
print(word)
word_guessed = ['_']*len(word)
print(word_guessed)

# Call the ask_for_input function to start the process of getting the user input and checking if the letter is in the random word.
ask_for_input()

