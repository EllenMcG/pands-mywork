# salaries_histogram.py
# This program generates a list of 100 random salaries in the range of 
# 20000-80000 using np.random.randint and plots them on a histogram

# Author Ellen McGrory

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

salaries = np.random.randint(20000,80000,100)
plt.hist(salaries)
plt.show()