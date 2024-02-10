# This program just prints out the addition of two inputs intergers - lab 3.1
# Author Ellen McGrory

# both inputs are converted to intergers so that they can be subtracted from each other
first_number = int(input("Enter first number: ")) 
second_number = int(input("Enter Second Number: "))


# subtract the two numbers
number_addition = first_number - second_number

print(f"{first_number} minus {second_number} is {number_addition}")

# Alternatively syntax can be ran as below for final output
# print("{} minus {} is {} ".format(first_number, second_number, number_addition))