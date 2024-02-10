# This program just prints out a random fruit from a list using the random package - lab 3.1
# Author Ellen McGrory
 
import random 
fruit_list = ['Apple', 'Orange', 'Banana', 'Pear', 'Cherry'] 

# Generating a random number for each fruit 

index = random.randint(0,len(fruit_list)-1) 

random_fruit = fruit_list[index] 
print(f"A Random Fruit: {random_fruit}")