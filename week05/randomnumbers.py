# randomnumbers.py
# This program takes 10 random numbers into a list called queue. One of the 
# random numbers is then removed and the list is printed. This is repeated sequentially
# until the queue of numbers is empty
# Author Ellen McGrory

import random 
queue = [] 
number_in_queue=10 
upper_range=100 

for n in range(0,number_in_queue):
    queue.append(random.randint(0,upper_range)) 

print (f"queue is {queue}") 

while len(queue) != 0: 
    current_number = queue.pop(0) 
    print (f"current Number is {current_number} and the queue is {queue} ") 

print ("the queue is now empty")
