# average.py
# This progam keeps reading in numbers until the user enter a 0
# The program then gets their average
# Author Ellen McGrory

numbers = []

number = int(input(f"Enter number (0 to quit): "))

while number != 0:
    numbers.append(number)
    number = int(input(f"Enter another number (0 to quit): "))

for value in numbers:
    print(value)

average = float(sum(numbers))/len(numbers)
print(f"The average is {average}")

