# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random
import unittest
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():

    randomWord = random.choice(FIVE_LETTER_WORDS).upper()
    

    def enter_action(s):
        #gw.show_message("You have to implement this method.")
        word = ""
        for x in range(0, 5): 
            word = word + gw.get_square_letter(N_ROWS-6, x)

        if word.lower() in FIVE_LETTER_WORDS:
            gw.show_message("Congrats!!! That is a word!")
        else:
            gw.show_message("Not a word in list")

    gw = WordleGWindow()
    y = 0
    for x in randomWord:
        gw.set_square_letter(N_ROWS-6, y ,randomWord[y])
        y += 1

    gw.add_enter_listener(enter_action)

# Startup code

if __name__ == "__main__":
    wordle()
    unittest.main(module="test_wordle")
