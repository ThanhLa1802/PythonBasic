import random
import string # xu ly chuoi ky tu
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
    alphabet = set(string.ascii_uppercase)

    user_letters = set()
    lives  = 5 
    while len(word_letters) > 0 and lives > 0:
        word_list = [letter if letter in user_letters else '_' for letter in word]

        print('Current word is: ',' '.join(word_list))

        user_letter = input('Guess your letter: ').upper()

        if user_letter in alphabet - user_letters: 
            user_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print(' ')
            else:
                lives -= 1
                print("You guessed wrong!", user_letter) 
        elif user_letter in user_letters:
            print("\nYou guessed that letter! Guess other guess:")
        else:
            print('\nYou guess invalid letter!')
    
    time.sleep(1)
    if lives == 0:
        print("You loss! The word is:", word)
    else:
        print("You will !!!!! The word is:", word)

hang_man()