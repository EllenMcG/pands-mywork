# useFib.py
# This program prompts the user to add a number so that the fibanacci function is run from the myFunctions module

# Author Ellen McGrory

import myFunctions

number_times = int(input('how many numbers in the Fibonacci do you need:'))
print(myFunctions.fibonacci(number_times))