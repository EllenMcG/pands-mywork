# topthree.py
# This progam generates 10 random numbers in range (0-100) and print out the 
# top three numbers
# Author Ellen McGrory

number_of_numbers = 10
top_numbers = 3
range_min_value = 0
range_max_value = 100

import random
numbers = []

for i in range(0,number_of_numbers):
    numbers.append(random.randint(range_min_value,range_max_value))
print(f"{number_of_numbers} random numbers\t {numbers}")

top_three = numbers.copy()

top_three.sort(reverse=True)
print(f"The top {top_numbers} are \t\t {top_three[0:top_numbers]}")
