# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

## Installation
To play Hangman, clone this repository to a directory of your choosing. This repository has a dependency on the random module, this is a in-built Python module.
Follow the [Usage](#usage) section to see how the Hangman project is used.

## Usage
Once you have this repository on your local machine you now have the ability to play Hangman!

You have two options to play the Hangman game:
1. Play the Hangman game with the default set of words.
2. Play the Hangman game with your own list of words, or a generated word list from a dataset.

### Playing the game with the default set of words.
Within the repository there is the ``` milestone_5.py ``` file. This file defines the Hangman class and it's methods, you can run ``` python -c 'import milestone_5; help(milestone_5)' ``` in the terminal to see the Class documentation.

Or alternatively, you can create a script within the same directory and import the module to this script and view the documention by running it, like so:

![](/pictures/HangmanImportScreen.png)

To play the game with the default set of words, all you have to do is call the ``` milestone_5.py ``` file from the terminal when you are in the repository. Like so:

![](/pictures/PlayHangmanDefaultScreen.png)

### Playing the game with your own set of words.
You can play the game with a custom set of words, by creating your own script within the repository and importing the module as above.
When the module is imported you can create your own word list, or even create a list from a dictionary dataset to use.
The following example shows the custom word list being created and how to run the game by passing this word list as a parameter.

![](/pictures/PlayHangmanCustomList.png)

Here, the ```milestone_5.py``` module is imported into the script, the custom list of words has been assigned to the variable ```word_list``` and the ```play_game()``` method is called with ```word_list``` passed as an argument. If this script is then run from the terminal, you are able to play a Hangman game with your custom list of words.

![](/pictures/CustomHangmanGame.png)
