# timesheetentry.py
# This program creates a class with three attributes 

# Author Ellen McGrory

import datetime as datetime

class Timesheetentry:
    def __init__(self, project, start, duration):
        self.project = project
        self.start = start
        self.duration = duration
    def __str__(self):
        return self.project +':' +str(self.duration )

# Writing a test case for the Timesheetentry class
if __name__ == '__main__':
    start_time = datetime.datetime(2021,3,19,16,29)
    test = Timesheetentry('test project', start_time , 60)
    print(test)