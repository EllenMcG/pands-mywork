# function_xsquared.py
# This program plots the function y = x^2 using matplotlib

import matplotlib.pyplot as plt
import numpy as np

x_data = np.array(range(1,101))
y_data = x_data * x_data

plt.plot(x_data,y_data)
plt.show()


