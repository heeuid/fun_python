#!/usr/bin/env python3

import random
import os

TITLE = '''
88                                                                            
88                                                                            
88                                                                            
88,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYb,d8 88,dPYba,,adPYba,  ,adPPYYba, 8b,dPPYba,
88P'    "8a ""     `Y8 88P'   `"8a a8"    `Y88 88P'   "88"    "8a ""     `Y8 88P'   `"8a
88       88 ,adPPPPP88 88       88 8b       88 88      88      88 ,adPPPPP88 88       88
88       88 88,    ,88 88       88 "8a,   ,d88 88      88      88 88,    ,88 88       88
88       88 `"8bbdP"Y8 88       88  `"YbbdP"Y8 88      88      88 `"8bbdP"Y8 88       88
                                    aa,    ,88                                
                                     "Y8bbdP"                                 
'''

stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''']

#Word bank of animals
words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

def replace_all(dest: list[str], comp: str, ch: str):
    cnt = 0
    for (i, c) in enumerate(comp):
        if dest[i] == '_' and c == ch:
            dest[i] = ch
            cnt += 1
    return cnt


def main():
    # Choose a word
    ans_word = random.choice(words)

    # Render Title
    print(TITLE)
    input("\nPress Enter to start a game.\n")

    # init
    life = len(stages)
    ur_answer = list("_" * len(ans_word))
    found = 0

    # Print blanks & render 
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        #print(ans_word)

        # blanks
        print("Your answer: ", ur_answer, sep = '')

        # stages
        print(stages[-life])    

        if life == 1 or found == len(ans_word):
            break

        # question
        alphabet = input("Please guess an alphabet: ")

        # input check
        if not alphabet.isalpha():
            continue
        else:
            alphabet = alphabet.lower()

        # check if right
        if alphabet in ans_word: # right
            found += replace_all(ur_answer, ans_word, alphabet)
        else: # wrong
            life -= 1

    print("Game Over: ", end = '')

    if life == 1:
        print("You Loose!")
    else:
        print("You Win!")

    input("\n(Press Enter to quit)")


main()
