# This file is for the milestone 5 section of the Hangman Project
# Import modules
import random

# Create the Hangman class
class Hangman:
    # Initialise the class attributes
    def __init__(self, word_list, num_lives = 5):
        self.word = random.choice(word_list) # Chosen random word
        self.word_guessed = ['_']*len(self.word) # Letters of the word guessed
        self.num_letters = len(set(self.word)) # Number of unique letters in the word that have not been guessed
        self.num_lives = num_lives # Number of lives
        self.word_list = word_list # Word list
        self.list_of_guesses = list() # List of guessed characters.

    # Create the check_guess method
    def check_guess(self, guess):
        guess = guess.lower()

        # Check if the letter is in the random word.
        if guess in self.word:
            print(f'Good guess! {guess} is in the word.')
            # Loops over the word, and creates an index. Replaces the blanks in the word_guessed list with the correct letter guessed.
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f'Sorry, {guess} is not in the word. Try again.')
            print(f'You have {self.num_lives} lives left.')            

    # Create the ask_for_input method
    def ask_for_input(self):
    # Create a while loop that asks a user for an input, check if the input is valid.
        while True:
            # Get the user input
            guess = input('Please guess a letter: ')

            # Check if the input meets the valid criteria
            if len(guess) != 1 or guess.isalpha() != True:
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

# Creates the Hangman object to pass through for the script to run.
word_list = Hangman(['passion fruit', 'strawberry', 'apple', 'banana', 'mango'])
Hangman.ask_for_input(word_list)


