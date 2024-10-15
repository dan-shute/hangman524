# This file is for the milestone 3 section of the Hangman Project.
# Import modules
import random

# Create the fruit list
word_list = ['passion fruit', 'strawberry', 'apple', 'banana', 'mango']

# Use the random module to choice a word from the list at random.
word = random.choice(word_list)
print(word)

# Create a while loop that asks a user for an input, check if the input is valid.
while True:
    # Get the user input
    guess = input('Please enter a single letter guess: ')

    # Check if the input meets the valid criteria
    if len(guess) == 1 and guess.isalpha() == True:
        break
    else:
        print('Invalid letter. Please, enter a single alphabetical character.')

# Check if the letter is in the random word.
if guess in word:
    print(f'Good guess! {guess} is in the word.')
else:
    print(f'Sorry, {guess} is not in the word. Try again.')