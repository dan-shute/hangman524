# This file is for the milestone 4 section of the Hangman Project
# Import modules
import random

# Create the Hangman class
class Hangman:
    def __init__(self, word_list, num_lives = 5):
        #attributes
        self.word = random.choice(word_list) # Chosen random word
        self.word_guessed = ['_']*len(self.word) # Letters of the word guessed
        self.num_letters = len(set(self.word)) # Number of unique letters in the word that have not been guessed
        self.num_lives = num_lives # Number of lives
        self.word_list = word_list # Word list
        self.list_of_guesses = list() # List of guessed characters.

    


