# guess1.py
# This program makes the user keep guessing a number until the correct predefined 
# number is reached - Lab 4.2
# Author Ellen McGrory

number_to_guess = 13
guess = int(input("Please guess the number: ")) 
while guess != number_to_guess: 
    print (f"Wrong") 
    guess = int(input("Please guess again: ")) 
print (f"Well done! Yes the correct number was {number_to_guess}")