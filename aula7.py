import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('./data/DimR00.csv')

print('DATA FRAME INICIAL')

print(df.head(10), end='\n\n')

#plt.plot(df['x'])
#plt.show()

print(df.columns)

print('AFTER DIMENTIONALITY REDUCTION')

# a = pd.cut(df['x'], 8)
# df['x'] = a

#df['x'] = df['x'].astype(int)

df['x'] = round(df['x'])

print(df.head(10))

plt.plot(df['x'])
plt.show()