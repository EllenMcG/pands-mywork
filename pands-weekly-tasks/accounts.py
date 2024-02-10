# This program an input 10 digit account number as a string and returns the account number with only the last four digits visible as an output
# the other digits are replaced by an X
# Author Ellen McGrory

# This program takes the last four digits by indexing to the 6-10 or last four digits of the input account number
# input_account_number = str(input("Please enter a 10 digit account number: "))
# print(f"XXXXXX{input_account_number[6:10]}")


# The program is rewritten to get the last 4 digits of an account number of differing length so the abolve indexing will 
# not work. Negative indexing will work and research to find this solution to the problem was done with assistance from the pointer
# (URL: https://thispointer.com/python-how-to-get-last-n-characters-in-a-string/)


input_account_number2 = str(input("Please enter an account number: "))
last_4_characters = input_account_number2[-4:]
print(f"XXXXXX{last_4_characters}")

