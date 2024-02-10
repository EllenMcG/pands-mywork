# This program just prints out the division of two numbers and gives a remainder - lab 3.1
# Author Ellen McGrory

# both inputs are converted to intergers so that they can be added
first_number = int(input("Enter first number: ")) 
second_number = int(input("Enter the number you want to divide by: "))


# Divide the two numbers and returns the integer
number_division = int(first_number//second_number)

# returns the remainder of the division operation
remainder = first_number%second_number

print(f"{first_number} divided by {second_number} is {number_division} with remainder {remainder}")