# Number Guessing Game - computer picks a number at random and the player tries to guess it.

import random

number = random.randint(1, 100) # Computer picks the number at random
attempts = 0 # variable to keep track of how many times it takes user to guess ti right

while True: # loop until number is correct
    guess = input("Guess a number between 1 and 100: ")
    if not guess.isdigit(): # check user input is a number
        print("Please enter a valid number only!")
        continue
    guess = int(guess)
    attempts += 1
    
    if guess < number: # 100 is alot of numbers so adding tips to make the game more enjoyable
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed it in {attempts} tries.")
        break