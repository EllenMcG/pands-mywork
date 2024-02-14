# guess3.py
# This program makes the user keep guessing a number until the correct number
# number is reached. At each guess the program gives hints if number is too low or high - Lab 4.2
# The correct number will be generated using a random number in the range 1-100 using the random package
# Author Ellen McGrory

# import the random package
import random
number_to_guess = random.randint(1,100)

guess = int(input("Please guess the number: ")) 
while guess != number_to_guess: 
    if guess < number_to_guess: 
        print(f"too low") 
    else: 
        print(f"too high") 
    guess = int(input(f"Please guess again: ")) 

print(f"Well done! Yes the correct number was {number_to_guess}")