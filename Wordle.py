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
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

#Wordle function that runs the game
def wordle():

    #Selecting the random word
    randomWord = random.choice(FIVE_LETTER_WORDS).upper()
    hardWord = []
    for x in randomWord:
        hardWord.append("")

    def enter_action(s):
        if gw.hard_mode_status() == False: # Regular Mode
            word = ""
            for x in range(N_COLS): 
                word += gw.get_square_letter(gw.get_current_row(), x)

            #Validating if it is a word
            if word.lower() in FIVE_LETTER_WORDS:
                #gw.show_message("Congrats!!! That is a word!")
                for x in range(N_COLS):
                    currentLetter = gw.get_square_letter(gw.get_current_row(), x)
                
                    if currentLetter == randomWord[x]:
                        gw.set_square_color(gw.get_current_row(), x,CORRECT_COLOR)
                    elif currentLetter in randomWord:
                        gw.set_square_color(gw.get_current_row(), x, PRESENT_COLOR)
                    else: 
                        gw.set_square_color(gw.get_current_row(), x, MISSING_COLOR)
                temp = gw.get_current_row() + 1
                gw.set_current_row(temp)

            else:
                gw.show_message("Not a word, try again")

            if word == randomWord:
                gw.show_message("Congrats!!! You Win!!")
            
        else: # Hard Mode
            word = ""
            for x in range(N_COLS):
                word += gw.get_square_letter(gw.get_current_row(), x)
                if hardWord[x] != "":
                    if word[x] != hardWord[x]: # Check that letter submitted matches letters found (issue)
                        gw.show_message("Must use found correct letters","Red")
                        return

            #Validating if it is a word
            if word.lower() in FIVE_LETTER_WORDS:

                for x in range(N_COLS):
                    currentLetter = gw.get_square_letter(gw.get_current_row(), x)
                
                    if currentLetter == randomWord[x]:
                        hardWord[x] = currentLetter
                        gw.set_square_color(gw.get_current_row(), x,CORRECT_COLOR)
                    elif currentLetter in randomWord:
                        gw.set_square_color(gw.get_current_row(), x, PRESENT_COLOR)
                    else: 
                        gw.set_square_color(gw.get_current_row(), x, MISSING_COLOR)
                temp = gw.get_current_row() + 1
                gw.set_current_row(temp)

                for x in range(N_COLS):
                    if "".join(hardWord) == word:
                        continue
                    if hardWord[x] != "":
                        gw.set_square_letter(gw.get_current_row(), x,hardWord[x])
                        gw.set_square_color(gw.get_current_row(), x,CORRECT_COLOR)

            else:
                gw.show_message("Not a word, try again")

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
