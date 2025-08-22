import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import pandas as pd 

data = {
    'Size_sqft': [1000, 1200, 1500, 1700, 2000],
    'Bedrooms': [2, 2, 3, 4, 3],
    'Age': [10, 5, 15, 20, 8],
    'Price': [300000, 320000, 400000, 450000, 500000]
}

df = pd.DataFrame(data)

X = df[['Size_sqft', 'Bedrooms', 'Age']]
y = df['Price']


model = LinearRegression()
model.fit(X,y)


new_data = pd.DataFrame({
    'Size_sqft': [1600, 1400, 1800],
    'Bedrooms': [3, 2, 4],
    'Age': [12, 10, 15]
})

predicted_prices = model.predict(new_data)
new_data['Predicted_Price'] = predicted_prices

print(df)
print(new_data)

