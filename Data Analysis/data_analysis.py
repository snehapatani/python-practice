import pandas as pd

df = pd.read_csv("data/people.csv")

print(df.head())

print("Mean Age", df['Age'].mean())
print("Max Salary", df['Salary'].max())
print("Min Salary", df['Salary'].min())

filtered_age = df[df['Age'] > 25]

print("Filtered Age\n", filtered_age)

filtered_sex = df[df['Sex'] == 'F']
print("Filtered Sex \n", filtered_sex)

filtered_city = df[df['City'] == 'San Francisco']
print("Filtered City \n", filtered_city)
 
print("Data Types of each column \n", df.dtypes)

print("Columns \n", df.columns)

print("Shapes\n", df.shape)

x=[1, 2, 3]
print(x * 2)