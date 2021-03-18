import random
import time
print("Welcome to RSL Game!")
time.sleep(1)
name = input("Please input your name: ")

print(f"Hello {name} !")

player_guess = 0
computer_guess = 0

while player_guess != 'e':
    player_guess = input("Select scissor - s, rock - r, leaf -l, exit -e \n")
    time.sleep(1)
    computer_guess = random.randint(1,3)
    if player_guess == 'e':
        print("See you again!")
        exit()
    if computer_guess == 1:
        computer_guess = 's'
    elif computer_guess == 2:
        computer_guess = "r"
    else:
        computer_guess = 'l'
    if computer_guess == player_guess:
        print("Draw!!!")
    elif computer_guess == 's' and player_guess == 'l':
        print(f"Player loss! Compuert guess: {computer_guess}")
    elif computer_guess == 's' and player_guess == 'r':
        print(f'Player win! Compuert guess: {computer_guess}')
    elif computer_guess == 'r' and player_guess == 's':
        print(f"Player loss! Compuert guess: {computer_guess}")
    elif computer_guess == 'r' and player_guess == 'l':
        print(f'Player win! Compuert guess: {computer_guess}')
    elif computer_guess == 'l' and player_guess == 'r':
        print(f"Player loss! Compuert guess: {computer_guess}")
    elif computer_guess == 'l' and player_guess == 's':
        print(f'Player win! Compuert guess: {computer_guess}')        
    