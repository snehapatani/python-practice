import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

X = np.array([[1000, 2, 10],
              [1500, 3, 5],
              [1200, 2, 20],
              [1700, 4, 15],
              [2000, 3, 8]])
y = np.array([300000, 400000, 320000, 450000, 500000])

model = LinearRegression()
model.fit(X,y)

y_pred = model.predict(X)

# Plot
plt.scatter(y, y_pred, color='blue')
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--')  # perfect prediction line
plt.xlabel('Actual Price')
plt.ylabel('Predicted Price')
plt.title('Predicted vs Actual Prices')
plt.show()