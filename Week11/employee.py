# employee.py
# This program creates a class called Employee that returns the
# first and last name of an employee and has a test case associated 
# with it

# Author Ellen McGrory

import datetime as datetime

class Employee:
    timesheets = []
    def __init__(self, first, last):
        self.first = first
        self.last = last
    def __str__(self):
        return self.first + ' ' + self.last

# Test case 
if __name__ == '__main__':
    test = Employee('John','Doe')
    print(test)
    assert('John Doe' == str(test))
