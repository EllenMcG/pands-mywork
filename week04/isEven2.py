# isEven2.py
# This program checks if an input number is odd or even, but looks for -1 first  
# This is a modified program of isEven.py that looks for -1 and wont check any interger in the 
# if loop unless its -1 - Lab 4.1
# Author Ellen McGrory

number = int(input("Enter an integer: ")) 
while number != -1: 
        number = int(input("Enter -1:"))
if (number % 2) == 0: 
        print(f"{number} is an even number") 
else: 
        print(f"{number} is an odd number")