import pandas as pd

df = pd.read_csv('data.csv')
print(df.head())

media = df['coluna'].mean()
print("Média da coluna: ", media)