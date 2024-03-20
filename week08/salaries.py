# salaries.py
# This program generates a list of ten random salaries in the range of 
# 20000-80000 using np.random.randint

# Author Ellen McGrory

import numpy as np

salaries = np.random.randint(20000,80000,10)
print(salaries)


# the program is then modified so that the same random numbers
# (pseudo-random) are returned again using the seed function of numpy
# The seed functionality is good for splitting data into repeatable chunks such 
# as for testing and training datasets

np.random.seed(42)
salaries = np.random.randint(20000,80000,10)
print(salaries)


# The program is now modified to add an additional 5000 to every
# number in the numpy array

salaries_bonus = salaries + 5000 
print(salaries_bonus)

# The program is now modified so that salaries are increased by 5%

salaries_increment = salaries * 1.05
print(salaries_increment)

salaries_increment_int = salaries_increment.astype(int)
print(salaries_increment_int)