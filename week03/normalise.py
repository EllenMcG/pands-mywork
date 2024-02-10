# This program strips any leading or trailing spaces of an input string, converts all letters to lower case
# and finds the length of the origional string and the normalised string - Lab 3.3
# Author Ellen McGrory

input_string = input("Please enter a string: ")
normalised_string = input_string.strip().lower()
length_of_raw_string = len(input_string)
lenght_of_normalised_string = len(normalised_string)

# Output
print(f"That string normalised is: {normalised_string}")

print(f"we reduced the input string length from {length_of_raw_string} to {lenght_of_normalised_string} characters")