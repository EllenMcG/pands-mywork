# collatz.py 

# This program calculates the  Collatz Conjecture. The Collatz Conjecture is a famous unsolved problem within mathematics 
# that takes a positive interger and if it is even (i.e, it the remainder is 0 when divided by 2 ( in the below program 
# this is done using the modulo operator to check if the remainder is 0 using num%2==0) it is then be divided by 2, 
# else it is odd. If the interger is odd then it is multiplied by 3 and 1 is added. The interesting part about
# the Collatz Conjecture is that the last three digits are always 4,2,1 in that sequence, however it hasn't being proved 
# that there is not an interger value that dosn't have this terminal sequence. The below program starts with a while statement
# to start the if/else loop only if the input number is not 1. It is stopped then as otherwise it will stay in the loop for the 
# 4,2,1 sequence. 

# Background reading on the problem: https://mathworld.wolfram.com/CollatzProblem.html
# Webpages used to assist in coding this problem
# 1) https://hackernoon.com/implementing-3x1-in-python
# 2) https://exercism.org/tracks/python/exercises/collatz-conjecture/dig_deeper
# 3) https://www.r-bloggers.com/2019/03/learning-r-the-collatz-conjecture/

# Author Ellen McGrory


num = int(input('Please enter a positive integer: '))
sequence = [num] # numbers stored in a python array
while(num != 1): # This while statement start the loop if the interger is not 1, else the program will be stuck in a loop of
    # 4,2, and 1. The if/else statement works here as only two outcomes, odd or even numbers
    if((num%2)==0): # To check for even number
        num = num // 2 
    else: # else part of statement is for running the odd number, 3N+1
        num = (num*3) + 1
    sequence.append(num)
print(sequence) # Prints the interger steps to reach the interger 1
