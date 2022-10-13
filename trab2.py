import pandas as pd
import numpy as np 

from sklearn.preprocessing import MinMaxScaler

df_standard = pd.read_csv('./data/vendas_lucro.csv')

print('STANDARD DF', end='\n\n')
print(df_standard.head, end='\n\n')

print('APPLYING MIN-MAX-SCALER', end='\n\n')

df_aux1 = df_standard['Vendas'].copy()
min_ = min(df_aux1)
max_ = max(df_aux1)

for i in range(len(df_aux1)):
    df_aux1[i] = (df_aux1[i] - min_) / (max_ - min_)

df_aux2 = df_standard['Lucro'].copy()
min_ = min(df_aux2)
max_ = max(df_aux2)

for i in range(len(df_aux2)):
    df_aux2[i] = (df_aux2[i] - min_) / (max_ - min_)

df_minmax = df_standard.copy()
df_minmax['Vendas'] = df_aux1
df_minmax['Lucro'] = df_aux2

print(df_minmax, end='\n\n')

print('APPLYING Z SCORE', end='\n\n')

df_aux1 = df_standard['Vendas'].copy()

mean = df_aux1.mean()
std = df_aux1.std()

for i in range(len(df_aux1)):
    df_aux1[i] = (df_aux1[i] - mean) / std

df_aux2 = df_standard['Lucro'].copy()

mean = df_aux2.mean()
std = df_aux2.std()

for i in range(len(df_aux2)):
    df_aux2[i] = (df_aux2[i] - mean) / std

df_z = df_standard.copy()
df_z['Vendas'] = df_aux1
df_z['Lucro'] = df_aux2

print(df_z, end='\n\n')

print('APPLYING INTERQUARTIL')

df_aux1 = df_standard['Vendas'].copy()
min_ = min(df_aux1)
max_ = max(df_aux1)

q1 = df_aux1.describe()['25%']
q2 = df_aux1.describe()['50%']
q3 = df_aux1.describe()['75%']


for i in range(len(df_aux1)):
    df_aux1[i] = (df_aux1[i] - q2) / (q3-q1)

df_aux2 = df_standard['Lucro'].copy()
min_ = min(df_aux2)
max_ = max(df_aux2)

q1 = df_aux2.describe()['25%']
q2 = df_aux2.describe()['50%']
q3 = df_aux2.describe()['75%']

for i in range(len(df_aux1)):
    df_aux2[i] = (df_aux2[i] - q2) / (q3-q1)

df_qt = df_standard.copy()
df_qt['Vendas'] = df_aux1
df_qt['Lucro'] = df_aux2

print(df_qt, end='\n\n')

print('TODOS JUNTOS', end='\n\n')
print(pd.concat([df_minmax, df_z, df_qt]))