import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 5, 4, 5])

model = LinearRegression()
model.fit(X, y)

print("Intercept: ", model.intercept_)
print("Slope: ", model.coef_)

y_pred = model.predict(X)

# Plot
plt.scatter(X, y, color="red", label="Data")
plt.plot(X, y_pred, color="blue", label="Prediction Line")
plt.xlabel("Study Hours")
plt.ylabel("Scores")
plt.legend()
plt.show()