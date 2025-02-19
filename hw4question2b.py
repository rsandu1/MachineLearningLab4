# CISC 5800 Homework 4 Question 2b
# Robert Sandu

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

# Training data
X = np.array([
    [30, 0],  # Should be 0
    [50, 1],  # Should be 1
    [70, 1],  # Should be 0
    [80, 2],  # Should be 1
    [100, 1]  # Should be 1
])

y = np.array([0, 1, 0, 1, 1])  # Labels

# Train logistic regression model
model = LogisticRegression()
model.fit(X, y)

# Extract decision boundary coefficients
w1, w2 = model.coef_[0]
b = model.intercept_[0]

print(f"Optimal Classifier: {w1:.4f} * x1 + {w2:.4f} * x2 + {b:.4f} = 0")

# Make predictions
predictions = model.predict(X)
errors = np.sum(predictions != y)
print(f"Predictions:  {predictions} , Actual Values {y}")
print(f"Total misclassifications: {errors}")



