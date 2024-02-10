# This program takes a minus currency value in dollars and cents and returns the absolute value and in cents Lab 3.2
# Author Ellen McGrory

# Returns the absolute amount then divides by 100 to return the amount in cents
input_currency = float(input("Please Enter an amount: "))
absolute_currency = (abs(input_currency)) * 100

# Returns the amount in cent to zero decimal places
print(f"That amount in cent is: {absolute_currency:.0f}")