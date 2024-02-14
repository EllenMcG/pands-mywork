# guess2.py
# This program makes the user keep guessing a number until the correct predefined 
# number is reached. At each guess the program gives hints if number is too low or high - Lab 4.2
# Author Ellen McGrory

number_to_guess = 13
guess = int(input("Please guess the number: ")) 
while guess != number_to_guess: 
    if guess < number_to_guess: 
        print(f"too low") 
    else: 
        print(f"too high") 
    guess = int(input(f"Please guess again: ")) 

print(f"Well done! Yes the correct number was {number_to_guess}")