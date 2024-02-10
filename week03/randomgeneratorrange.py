# This program just prints out a randon number with a user defined range using the random package - lab 3.1
# Author Ellen McGrory

# import the random package
import random

# both inputs are converted to intergers so added to range
first_number = int(input("Enter first number in range: ")) 
second_number = int(input("Enter Second Number in range: "))

# Generate a random number in range defined by user
random_number = random.randint(first_number,second_number)

print(f"here is a random number {random_number}")