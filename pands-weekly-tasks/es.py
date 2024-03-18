# es.py
# This program takes a text file as input from the command line and counts the number of occurences the letter 'e' is present
# This program will use the 'sampletextfile.txt' than contains placeholder infromation (Lorem ipsum) that will be used to count the 
# number of e's in the file

# Author Ellen McGrory

# Two things are done to complete this piece of analysis. Firstly the sys module is used to give a filename in the command line. Using
# sys.argv[-1] gives a command line argument. The [-1] passes the last argument. 
# If no txt file is given, the analysis runs off the current script. 
# Background used to review these concepts
# URL: https://www.knowledgehut.com/blog/programming/sys-argv-python-examples#what-are-command-line-arguments?-why-do-we-use%C2%A0them?%C2%A0
# URL: https://stackoverflow.com/questions/7033987/get-a-file-from-cli-input

# Following this, the filename is then passed to a context manager (designated with the open) where the code below is then ran and 
# the code is executed. Following code execution, the context manager will then close the file (in this case sampletextfile.txt)
# Background used to review context manager
# URL: https://realpython.com/python-with-statement/

# The codeblock contains a for loop to break the text file into a series of lines, words and letters so that the individual number of e's
# are added to the 'numberof_es' count and are added at the end

import sys
filename = sys.argv[-1]

with open(filename,'rt') as filename:
    numberof_es=0
    for line in filename:
        words = line.split()
        for i in words:
            for letter in i:
                if (letter=='e'):
                    numberof_es=numberof_es+1
print(numberof_es)
