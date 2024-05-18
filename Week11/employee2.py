# employee2.py
# This program creates a class called Employee that returns the
# first and last name of an employee and has a test case associated 
# with it. This Employee class has two extra funtions within the class
# compared to employee.py

# Author Ellen McGrory

# Importing the Timesheetentry class from the timesheetentry.py script
# This will be used to return total minutes

from timesheetentry import *
import datetime as datetime

class Employee:
    timesheets = []
    def __init__(self, first, last):
        self.first = first
        self.last = last
    def __str__(self):
        return self.first + ' ' + self.last
    def logminutes(self, project, minutes):
        now = datetime.datetime.now
        timesheetentry = Timesheetentry(project, now, minutes)
        self.timesheets.append(timesheetentry)
    def gettotaltime(self):
        total_minutes = 0 
        for start_time in self.timesheets:
            total_minutes += start_time.duration 
        return total_minutes

# test case
if __name__ == '__main__':
    test = Employee('John', 'Doe')
    print(test)
    assert('John Doe' == str(test))
    test.logminutes('p1',30)
    test.logminutes('p2',60)
    mins = test.gettotaltime()
    print(mins)
    assert(mins == 90)
    print('All good')