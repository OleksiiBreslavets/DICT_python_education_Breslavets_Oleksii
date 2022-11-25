"""Hangman project: simple game"""

# Libraries
import random

# Functions
from error_check import error_check

# 8-th stage
print("\nHANGMAN")  # Program name

# List of words -- data for operations (actions)
programming = ("python", "java", "javascript", "php", "class", "method", "parameter", "constant", "header")

# First choice to play
menu = input("Type \"play\" to play the game, \"exit\" to quit: > ")

# Menu action
while menu != "exit":

    if menu != "play":
        print("Incorrect command! Try again!")
        menu = input("Type \"play\" to play the game, \"exit\" to quit: > ")
        continue

    # Using random-word and parameters
    word_guess = random.choice(programming)
    word_puzzled = "-" * len(word_guess)
    errors_num = 0
    other_symbols = ""

    # The main body of the program with errors checking
    while errors_num != 8 and "-" in word_puzzled:  # Check of maximum errors number
        print("\n" + word_puzzled)
        word_user = input("Input a letter: > ")  # The input of the letter

        check, other_symbols, errors_num = error_check(word_guess, word_puzzled, other_symbols, errors_num, word_user)

        if check:
            # Replace symbol with some index in the word
            word_puzzled = [word_user if val == word_user else word_puzzled[i] for i, val in enumerate(word_guess)]
            word_puzzled = "".join(str(e) for e in word_puzzled)

    else:
        if "-" not in word_puzzled:  # Check of guessing the word
            print("\n" + word_puzzled + "\nYou guessed the word!\nYou survived!")
        else:
            print("You lost!")

    menu = input("Type \"play\" to play the game, \"exit\" to quit: > ")
