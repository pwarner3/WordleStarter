# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
Aaron Petersen
Parker Smith
Lauren Likes
Parker Warner
"""

import random
import unittest
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():

    randomWord = random.choice(FIVE_LETTER_WORDS).upper()

    def enter_action(s):
        word = ""
        for x in range(N_COLS): 
            word += gw.get_square_letter(gw.get_current_row(), x)

        if word.lower() in FIVE_LETTER_WORDS:
            gw.show_message("Congrats!!! That is a word!")
            temp = gw.get_current_row() + 1
            gw.set_current_row(temp)
        else:
            gw.show_message("Not a word in list")

        if word == randomWord:
            gw.show_message("Congrats!!! You Win!!")

    gw = WordleGWindow()
    # y = 0
    # for x in randomWord:
    #     gw.set_square_letter(N_ROWS-6, y ,randomWord[y])
    #     y += 1

    gw.show_message(f"Word is: {randomWord}")

    gw.add_enter_listener(enter_action)


if __name__ == "__main__":
    wordle()
    unittest.main(module="test_wordle")
