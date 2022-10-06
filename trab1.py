import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.impute import SimpleImputer

df = pd.read_csv('./data/LD00c.csv')

print('DF INICIAL', end='\n')
print(df.head(10), end='\n\n')


# data sempre tem valor
# hora sempre tem valor (12h ou 0h)


#imputer1 = SimpleImputer(missing_values='nan', strategy=)

df.fillna(method='ffill', inplace=True)

print('DF PREENCHIDO', end='\n')
print(df.head(100), end='\n\n')

print('DESCRICAO DO DATAFRAME', end='\n\n')
print(df.info())

print('MEDIA TOTAL, MAXIMO, MINIMO', end='\n')
print(df.describe(), end='\n\n')

# df.to_csv('./data/save')

insolacao = df['Insolacao']
dia = df['Data']
temp = df['TempMaxima']

print(f'O dia em que teve maior insolacao foi {dia[insolacao.idxmax()]} teve {insolacao.max()}')
print(f'O dia em que teve maior temperatura foi {dia[temp.idxmax()]} teve {temp.max()}')


print('EXCLUINDO OS OUTLIERS', end='\n\n')
df = df[df['TempMaxima'] < 45]
df = df[df['TempMinima'] > -10]

insolacao = df['Insolacao']
dia = df['Data']
temp = df['TempMaxima']

print('REPETINDO TESTES', end='\n\n')
print(f'O dia em que teve maior insolacao foi {dia[insolacao.idxmax()]} teve {insolacao.max()}')
print(f'O dia em que teve maior temperatura foi {dia[temp.idxmax()]} teve {temp.max()}')

min_temp = df['TempMinima']
plt.hist(min_temp)
plt.show()