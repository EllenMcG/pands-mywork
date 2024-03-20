# counties_bar.py
# This program generates a bar chart from a list of Irish counties based on code from counties.py

# Author Ellen McGrory

import numpy as np
import matplotlib.pyplot as plt

counties_list = ["Donegal", "Galway", "Clare", "Longford", "Sligo"]
counties = np.random.choice(counties_list,p=[0.3,0.2,0.2,0.1,0.2], size=100)

unique, counts = np.unique(counties, return_counts=True)

plt.bar(unique, counts)
plt.show()
