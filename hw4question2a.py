# CISC 5800 Homework 4 Question 2a
# Robert Sandu

import numpy as np
import matplotlib.pyplot as plt

# Training data
X = np.array([
    [30, 0],  
    [50, 1],  
    [70, 1],  
    [80, 2],  
    [100, 1]  
])

y = np.array([0, 1, 0, 1, 1])  # Labels

plt.figure(figsize=(10, 6))

# Plot data points
for i in range(len(X)):
    if y[i] == 0:
        plt.scatter(X[i][0], X[i][1], color='red', marker='o', label='Did Not Donate' if i == 0 else "")
    else:
        plt.scatter(X[i][0], X[i][1], color='blue', marker='x', label='Dontated' if i == 1 else "")

plt.xlabel("Income ($1000s)")
plt.ylabel("Websites Followed")
plt.legend()
plt.title("Scatter Plot of Political Donations")
plt.show()
