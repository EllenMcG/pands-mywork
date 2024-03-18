# counts.py
# This program counts the number of times a file was run (using 'count.txt')

# Author Ellen McGrory

FILENAME = "count.txt" 

def readNumber(): 
    with open(FILENAME) as f: 
        number = int(f.read()) 
        return number 

def writeNumber(number): 
    with open(FILENAME, "wt") as f: 
        f.write(str(number)) 
 
num = readNumber() 
num = num +1
print(f"we have run this program {num} times")
writeNumber(num)