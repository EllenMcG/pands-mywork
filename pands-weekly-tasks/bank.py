# bank.py 
# This program just prints out the addition of two inputs in cents
# and performs an addition on the two inputs and returns the 
# addition of the inputs as Euro recorded to two decimal places

# Author Ellen McGrory

# both inputs are converted to intergers so that they can be added
amount1 = int(input("Enter amount1(in cent):")) 
amount2 = int(input("Enter amount2(in cent):"))


# dividing by 100 to convert cent amount to Euro amount
total_amount = (amount1 + amount2)/100

# .2f indicates that rounding is done to two decimal places
# adding the euro sign using unicode character name

print(f"The sum of these is \N{euro sign}{total_amount:.2f}")