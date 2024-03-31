# weekday.py
# This program returns an output if it is a weekday or not 
# Author Ellen McGrory

# This python program using the datetime module available for python. The today() function checks what the date is today. The weekday()
# fuction is then applied which returns an interger of the day of the week from 0 (Monday) to 6 (Sunday). This can then be wrapped
# in an if/else statement. If the day value is less than 5 (i.e., day is in the range of 0 to 4 for Monday to Friday) then the first
# print statement is printed. If the first statement is false then the else statement takes over and it is the weekend, i.e., day has 
# a value of 5 or 6 (Saturday or Sunday)

# The SheCodes website was useful in order to get background to the datetime.today().weekday() functionality 
# URL: https://www.shecodes.io/athena/10185-how-to-check-what-day-of-the-week-it-is-in-python#:~:text=date%20using%20datetime.-,datetime.,%20to%206%20(Sunday

import datetime

day = datetime.datetime.today().weekday()

if day < 5:
    print(f"Yes, unfortunately today is a weekday")
else: 
    print(f"It is the weekend, yay!")

