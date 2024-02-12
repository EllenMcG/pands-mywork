# grade.py
# This program prints the the grade for a given percentile of a test - Lab 4.1
# Author Ellen McGrory

percentage = float(input("Enter the percentage: ")) 

if percentage < 0 or percentage > 100: 
    print("Please enter a number between 0 and 100") 
elif percentage < 40: 
    print("Fail") 
elif percentage < 50: 
    print("Pass") 
elif percentage < 60:
    print("Merit1") 
elif percentage < 70: 
    print("Merit2") 
else: 
    print("Distinction")