# counts2.py
# This program is an updated version of counts.py where the number of times a file was run (using 'count.txt')
# This program has an additional check on if the text file is present

# Author Ellen McGrory

import os.path 
FILENAME = "count.txt" 
if not os.path.isfile(FILENAME): 
    print ("File does not exist")  
    writeNumber(0)

def readNumber(): 
    try:
        with open(FILENAME) as f: 
            number = int(f.read()) 
            return number
    except IOError:
        return 0

def writeNumber(number): 
    with open(FILENAME, "wt") as f: 
        f.write(str(number)) 
 
num = readNumber() 
num = num +1
print(f"we have run this program {num} times")
writeNumber(num)