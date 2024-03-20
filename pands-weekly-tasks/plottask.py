# plottask.py
# This program uses matplotlib.pyplot to display a plot that shows both of the below;
# - a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, and
# - a plot of the function h(x)=x3 in the range 0 to 10

# The subplot function within matplotlib will be used to show the histogram on the left, and the scatter plot on the
# right hand side 

# Matplotlib source documentation was used for both scatterplots and histogram as well as subplots
# Scatter URL: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html
# Hist URL: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html
# Subplot URL: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html

# In addition, the documentation of rendering mathematical formula such as X^3 using latex was read and applied 
# in the below example
# Latex in Matplotlib URL: https://matplotlib.org/stable/gallery/text_labels_and_annotations/tex_demo.html

# Author Ellen McGrory

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

normal_distribution = np.random.normal(5,2,1000)

# Histrogram
plt.subplot(1,2,1)
plt.hist(normal_distribution, label="Normal Distribution",bins=20)
plt.title("Normal Distribution",fontsize=25)
plt.ylabel("Frequency", rotation=0,labelpad=40,fontsize=15)
plt.xlabel("Number",fontsize=15)
plt.legend(fontsize=10)


# Scatterplot
x_data = np.array(range(1,11))
y_data = x_data * 3

plt.subplot(1,2,2)
plt.scatter(x_data, y_data, label="$X^3$",color="r")
plt.title("$h(x) = x^3$",fontsize=25)
plt.xlabel("$X$",fontsize=15)
plt.ylabel("$x^3$",rotation=0,labelpad=20,fontsize=15)
plt.legend(fontsize=10)
plt.show()