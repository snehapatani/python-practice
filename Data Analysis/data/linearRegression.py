import numpy as np
import matplotlib.pyplot as plt

X = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])

m = len(X)



X_b = np.c_[np.ones((m, 1)), X]

print("X_b", X_b)
print("X_b.T Transpose", X_b.T)

theta = np.zeros(2)
alpha = 0.01
iterations = 1000

print("Theta", theta)

print("X_b.dot(theta)", X_b.dot(theta))


for _ in range(iterations):
    gradients = (1/m) * X_b.T.dot(X_b.dot(theta) - y)
    theta = theta - alpha * gradients

print("Learned Parameter Theta", theta)

y_pred = X_b.dot(theta)

print("y_pred", y_pred)

# Plot
plt.scatter(X, y, color="red", label="Data")
plt.plot(X, y_pred, color="blue", label="Prediction Line")
plt.xlabel("Study Hours")
plt.ylabel("Scores")
plt.legend()
plt.show()