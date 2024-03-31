# This program an input 10 digit account number as a string and returns the account number with only the last four digits visible as an output
# the other digits are replaced by an X
# Author Ellen McGrory

# This program takes the last four digits by indexing to the 6-10 or last four digits of the input account number
# input_account_number = str(input("Please enter a 10 digit account number: "))
# print(f"XXXXXX{input_account_number[6:10]}")


# The above program is rewritten to get the last 4 digits of an account number of differing length so the abolve indexing will 
# not work. Negative indexing will work and research to find this solution to the problem was done with assistance from the pointer
# (URL: https://thispointer.com/python-how-to-get-last-n-characters-in-a-string/)

# The second problem was how to change the number of X's returned with a variable account number. This was done with a lot of trail and 
# error and the best way I've found to do it was to get to length of the input string and take 4 away from it. This returns the number of 
# X's to be placed before the last few digits. I coud then used that number to multiply the number of X's required so that now I can return
# any account number of variable length and the last four digts will be returned by negative indexing and the number of X's is returned 
# using a calculation

input_account_number2 = str(input("Please enter an account number: "))
last_4_characters = input_account_number2[-4:]
length_of_account_num = len(input_account_number2) - 4 
number_of_X = length_of_account_num * 'X'
print(f"{number_of_X}{last_4_characters}")

