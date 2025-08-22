import pandas as pd
from sklearn.linear_model import LogisticRegression

data = {
    'Hours_Studied': [2,4,6,8,7,3],
    'Sleep_Hours': [9,6,7,5,8,7],
    'Pass': [0,0,1,1,1,0]
}

df = pd.DataFrame(data)

X = df[['Hours_Studied', 'Sleep_Hours']]
y = df['Pass']

model = LogisticRegression()
model.fit(X,y)

new_data = pd.DataFrame({
    'Hours_Studied': [5,9],
    'Sleep_Hours': [6,2]
})

pred_class =  model.predict(new_data)
pred_proba = model.predict_proba(new_data)

new_data['Pass'] = pred_class

print("Predicted Class:", pred_class)
print("Probability:", pred_proba)

print(df)
print(new_data)


