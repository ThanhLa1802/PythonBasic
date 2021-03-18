import random
name = input("Please input your name: ")

print(f"Welcome {name} to Guess Number Game!")

guess_number = 0

com_guess = random.randint(1,50)
count = 0
while guess_number != com_guess:
    guess_number = int(input("Please input your number 1 - 50: "))
    count += 1
    if count > 4:
        print("Time up!!!")
        exit()
    if guess_number < com_guess:
        print("You guess too low!")
    if guess_number > com_guess:  
        print("You guess too high!")
    
print("Amazing Good Job!!!")
print(f"Computer guess is: {com_guess}")