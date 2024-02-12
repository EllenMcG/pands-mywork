# grade2.py
# This program prints the the grade for a given percentile of a test - Lab 4.1
# THis updated program handles rounded values so that a grade of 69.8 would be rounded to a distinction and not a merit2
# Author Ellen McGrory

percentage = round(float(input("Enter the percentage: ")),0) 
# The input is rounded to a whole number before passed to the if statement so that grades are rounded

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