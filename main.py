import pandas as pd

df = pd.read_csv('World-happiness-report-2024.csv')

print(df.head())

print(df.info())

print(df.describe())

df = pd.read_csv('dz.csv')
df.fillna(0, inplace=True)
print(df.head(10))

avg = df.groupby('City')['Salary'].mean()
print(avg)
