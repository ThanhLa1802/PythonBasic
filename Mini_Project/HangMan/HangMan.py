import random
import string
import time
from words import words

def get_valid_word(str):
    word = random.choice(str)
    while '_' in word or ' ' in word:
        word = random.choice(str)
    return word.upper()

def hang_man():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set (string.ascii_uppercase)
    user_letters = set()
    lives = 5
    while len(word_letters) > 0 and lives > 0:
        #word_list = [letter if letter in use_letters else '_' for letter in word]
        word_list = []
        for letter in word:
            if letter in user_letters:
                word_list.append(letter)
            else:
                word_list.append('_')
        print('Current word is:',' '.join(word_list))
        guess_letter = input("Guess your letter: ").upper()
        if guess_letter in alphabet - user_letters:
            user_letters.add(guess_letter)
            if guess_letter in word_letters:
                word_letters.remove(guess_letter)
                print(" ")
            else:
                lives -= 1
                print(f'You guess wrong! Times is {lives}')
        elif guess_letter in user_letters:
            print("\nYou guessed letter! Guess other: ")
        else:
            print("\nYou get invalid letter!")
    time.sleep(1)
    if lives == 0:
        print("You loss! The word is: ", word)
    else:
        print("You win!!!! The word is: ", word)

hang_man()
