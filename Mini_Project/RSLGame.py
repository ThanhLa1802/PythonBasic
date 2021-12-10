import random
import time

print("Welcome to OAN TU XI GAME !!!")
time.sleep(1)

player_name = input("Please input your name: ")
print(f"Hello {player_name} !!!")
player_choose = 0
computer_choose = 0

while player_choose != 'e':
    player_choose = input('SELECT KEO - s, DA - r, LA - l, EXIT - e \n')
    time.sleep(1)
    computer_choose = random.randint(1, 3)
    if player_choose == 'e':
        print("See you again!")
        exit()
    if computer_choose == 1:
        computer_choose = 's'
    if computer_choose == 2:
        computer_choose = 'r'
    if computer_choose == 3:
        computer_choose = 'l'
    if computer_choose == player_choose:
        print("Draw !!!")
    elif computer_choose == 's' and player_choose == 'l':
        print(f"Player loss! Compuert guess: {computer_choose}")
    elif computer_choose == 's' and player_choose == 'r':
        print(f'Player win! Compuert guess: {computer_choose}')
    elif computer_choose == 'r' and player_choose == 's':
        print(f"Player loss! Compuert guess: {computer_choose}")
    elif computer_choose == 'r' and player_choose == 'l':
        print(f'Player win! Compuert guess: {computer_choose}')
    elif computer_choose == 'l' and player_choose == 'r':
        print(f"Player loss! Compuert guess: {computer_choose}")
    elif computer_choose == 'l' and player_choose == 's':
        print(f'Player win! Compuert guess: {computer_choose}')