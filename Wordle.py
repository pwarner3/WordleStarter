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
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, GameEndWindow

#Wordle function that runs the game
def wordle():

    #Selecting the random word
    randomWord = random.choice(FIVE_LETTER_WORDS).upper()
    hardWord = []
    for x in randomWord: # Initialize hard mode word
        hardWord.append("")

    def enter_action(s):

        if gw.hard_mode_status() == False: # Regular Mode
            rowDecrement = 0
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
                        gw.set_key_color(currentLetter,CORRECT_COLOR)
                    elif currentLetter in randomWord:
                        gw.set_square_color(gw.get_current_row(), x, PRESENT_COLOR)
                        gw.set_key_color(currentLetter,PRESENT_COLOR)
                    else: 
                        gw.set_square_color(gw.get_current_row(), x, MISSING_COLOR)
                        gw.set_key_color(currentLetter,MISSING_COLOR)

            else:
                gw.show_message("Not a word, try again")
                rowDecrement = 1

            if word == randomWord: # Win Condition
                
                numTries = gw.get_current_row() + 1
                global pw
                pw = GameEndWindow(numTries) 

                pw.show_message("Congrats! It took you " + str(numTries) + " attempt(s)!\n \nScreenshot to share with friends")
            
                
                for x in range(0, numTries):
                    for y in range(N_COLS):
                        color = gw.get_square_color(x, y)
                        pw.set_square_color(x, y, color)
                return

                

                
            
            temp = gw.get_current_row() + 1 - rowDecrement
            if temp == N_ROWS: # Lose Condition
                numTries = gw.get_current_row() + 1
                global lw
                lw = GameEndWindow(numTries) 

                lw.show_message(f"\n\n\n\nSorry, You Lost.\nThe Word was {randomWord} \n\nIt took you {numTries} attempt(s)!\n \nShare your results with friends!")
                
                for x in range(0, numTries):
                    for y in range(N_COLS):
                        color = gw.get_square_color(x, y)
                        lw.set_square_color(x, y, color)
                return
            gw.set_current_row(temp)




        else: # Hard Mode
            rowDecrement = 0
            word = ""
            for x in range(N_COLS):
                word += gw.get_square_letter(gw.get_current_row(), x)
                if hardWord[x] != "":
                   if word[x] != hardWord[x]: # Check that letter submitted matches letters found
                        gw.show_message("Must use found correct letters","Red")
                        rowDecrement = 1

            #Validating if it is a word
            if word.lower() in FIVE_LETTER_WORDS:

                for x in range(N_COLS):
                    currentLetter = gw.get_square_letter(gw.get_current_row(), x)
                
                    if currentLetter == randomWord[x]:
                        hardWord[x] = currentLetter
                        gw.set_square_color(gw.get_current_row(), x,CORRECT_COLOR)
                        gw.set_key_color(currentLetter,CORRECT_COLOR)
                    elif currentLetter in randomWord:
                        gw.set_square_color(gw.get_current_row(), x, PRESENT_COLOR)
                        gw.set_key_color(currentLetter,PRESENT_COLOR)
                    else: 
                        gw.set_square_color(gw.get_current_row(), x, MISSING_COLOR)  
                        gw.set_key_color(currentLetter,MISSING_COLOR)             

            else:
                gw.show_message("Not a word, try again")
                rowDecrement = 1

            if word == randomWord: # Win Condition

                numTries = gw.get_current_row() + 1
                global mw
                mw = GameEndWindow(numTries) 

                mw.show_message("Congrats! It took you " + str(numTries) + " attempt(s)!\n \nShare your results with friends!!!")
                
                for x in range(0, numTries):
                    for y in range(N_COLS):
                        color = gw.get_square_color(x, y)
                        mw.set_square_color(x, y, color)

            temp = gw.get_current_row() + 1 - rowDecrement # Incrememnt row to be new line (or stay on same one)
            if temp == N_ROWS: # Lose Condition
                numTries = gw.get_current_row() + 1
                global lhw
                lhw = GameEndWindow(numTries) 

                lhw.show_message(f"\n\n\n\nSorry, You Lost.\nThe Word was {randomWord} \n\nIt took you {numTries} attempt(s)!\n \nShare your results with friends!")
                
                for x in range(0, numTries):
                    for y in range(N_COLS):
                        color = gw.get_square_color(x, y)
                        lhw.set_square_color(x, y, color)
                return
            gw.set_current_row(temp)

            for x in range(N_COLS):
                
                if "".join(hardWord) == word:
                    continue
                if hardWord[x] != "":
                    gw.set_square_letter(gw.get_current_row(), x,hardWord[x])
                    gw.set_square_color(gw.get_current_row(), x,CORRECT_COLOR)
                    
                    

    gw = WordleGWindow()

    # For development only
    # gw.show_message(f"Word is: {randomWord}")

    gw.add_enter_listener(enter_action)


if __name__ == "__main__":
    wordle()
    unittest.main(module="test_wordle")
