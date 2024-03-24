# bank.py 
# This program just prints out the addition of two inputs in cents
# and performs an addition on the two inputs and returns the 
# addition of the inputs as Euro recorded to two decimal places

# Author Ellen McGrory

# The result can be stored as a float, but due to the way floats are stored
# floats are not a good way to store currency. While it may not cause an error (imprecision error)
# in the below format. When multiple addition, subtratation, etc operations are performed on the 
# currency value then these floats (or floating point numbers) imprecision can be added to the currency
# due to rounding errors. 
# For this reason, total amount will be returned as a decimal rather than a float using the decmimal package

# Background reading on floating point numbers and decimal module
# URL: https://husobee.github.io/money/float/2016/09/23/never-use-floats-for-currency.html
# URL: https://docs.python.org/3/library/decimal.html

from decimal import *

# both inputs are converted to intergers so that they can be added
amount1 = int(input("Enter amount1(in cent): ")) 
amount2 = int(input("Enter amount2(in cent): "))


# dividing by 100 to convert cent amount to Euro amount
total_amount = Decimal((amount1 + amount2)/100)

# .2f indicates that rounding is done to two decimal places
# adding the euro sign using unicode character name

print(f"The sum of these is \N{euro sign}{total_amount:.2f}")