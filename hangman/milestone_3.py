# This file is for the milestone 3 section of the Hangman Project.
# Import modules
import random

# Create a while loop that asks a user for an input, check if the input is valid.
while True:
    # Get the user input
    guess = input('Please enter a single letter guess: ')

    # Check if the input meets the valid criteria
    if len(guess) == 1 and guess.isalpha() == True:
        break
    else:
        print('Invalid letter. Please, enter a single alphabetical character.')