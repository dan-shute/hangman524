# Import modules
import random

# Create the fruit list
word_list = ['passion fruit', 'strawberry', 'apple', 'banana', 'mango']

# Use the random module to choice a word from the list at random.
word = random.choice(word_list)

# Print the selected word
print(word)

# Ask the user to input a single letter, place this input into the variable 'guess'
guess = input('Please enter a single letter: ')