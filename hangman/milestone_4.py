# This file is for the milestone 4 section of the Hangman Project
# Import modules
import random

# Create the Hangman class
class Hangman:
    def __init__(self, word_list, num_lives = 5):
        #attributes
        self.word = random.choice(word_list)
        self.word_guessed = ['_','_','_','_','_']
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = list()


