# ages2.py
# This program generates a random number of 100 ages and is used with the 
# salaries returned in salaries.py to generate a scatter plot using Matplotlib
# This program differs from ages.py with an addtional line being added and the plt.show()
# inserted later

# Author Ellen McGrory

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

salaries = np.random.randint(20000,80000,100)
ages = np.random.randint(low = 21, high = 65, size =100)

plt.scatter(ages, salaries)
plt.title("Scatter Plot of Age versus Salary")
plt.xlabel("Age (Years)")
plt.ylabel("Salary ($)")
#plt.show()

x_data = np.array(range(1,101))
y_data = x_data * x_data

plt.plot(x_data, y_data, color = 'r')
plt.show()