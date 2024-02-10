# This program just prints the rounded down value of a float usin the math package - Lab 3.2
# Author Ellen McGrory

# import the math package
import math

input_to_floor = float(input("Enter a float number: "))
floored_float = math.floor(input_to_floor)

print(f"{input_to_floor} floored is {floored_float}")