# This file is for the milestone 5 section of the Hangman Project
# Import modules
import random

# Create the Hangman class
class Hangman:
    '''
    This class is used to represent the Hangman instance, and allows the user to play a game of Hangman against the computer.

    Attributes:
        word_list (list): A list of words for the game to choose.
        word (str): The randomly chosen word from the word_list.
        word_guessed (list): A list of letters of the word, with '_' for each letter not yet guessed.
        num_letters (int): The number of UNIQUE letters in the word that have not yet been guessed.
        num_lives (int): The number of lives the player has at the start of the game.
        list_of_guesses (list): A list of guesses that have already been tried.
    '''
    # Initialise the class attributes
    def __init__(self, word_list, num_lives = 5):
        '''
        See help(Hangman) for accurate signature.
        '''
        self.word = random.choice(word_list) # Chosen random word
        self.word_guessed = ['_']*len(self.word) # Letters of the word guessed
        self.num_letters = len(set(self.word)) # Number of unique letters in the word that have not been guessed
        self.num_lives = num_lives # Number of lives
        self.word_list = word_list # Word list
        self.list_of_guesses = list() # List of guessed characters.

    # Create the check_guess method
    def check_guess(self, guess):
        '''
        This method is used to check if the guessed letter is within the randomly chosen word.
        If the letter is in the word then the attributes word_guessed and num_letters are updated.
        If the letter is not in the word then the attribute num_lives is updated.

        Args:
            guess (str): The user input guess.
        '''
        guess = guess.lower()

        # Check if the letter is in the random word.
        if guess in self.word:
            print(f'Good guess! {guess} is in the word.')
            # Loops over the word, and creates an index. Replaces the blanks in the word_guessed list with the correct letter guessed.
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = guess
            print(self.word_guessed)
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f'Sorry, {guess} is not in the word. Try again.')
            print(f'You have {self.num_lives} lives left.')            

    # Create the ask_for_input method
    def ask_for_input(self):
        '''
        This method is used to get the user input.
        Validation checks are made to ensure that the guess is a single alphabetical character, as well as checking that the guess has not already been made.
        If the guess is not a single alphabetical character, feedback is given and the user is asked to enter a valid character.
        If the guess has already been made, feedback is given and lets the user know they have already guessed that character.
        If all validation checks are passed the guess is passed into the check_guess method and the guess is added to the list_of_guesses attribute.
        '''
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
                self.list_of_guesses.append(guess) # Append the guessed letter to the list_of_guesses attribute.
                break

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    
    while True:
        if game.num_lives == 0: # If the user is out of lives, the user has lost. End the game. 
            print('You lost!')
            break
        if game.num_letters > 0: # If num_letters is greater than zero, the word still has remaining letters to be guessed. Continue the game by asking the user for the next input.
            game.ask_for_input()
        if game.num_lives !=0 and game.num_letters <= 0: # If the user still has lives, and there are no letters remaining to be guessed. The user has won. End the game.
            print('Congratulations. You won the game!')
            break

# if __name__ == '__main__' ensures that if this is called from this file directly, then this section of code is run.
# It passes in a default word_list and plays the game for the user.
if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon', 'passionfruit','plum']
    play_game(word_list)


