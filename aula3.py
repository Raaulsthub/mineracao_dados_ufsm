import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

nomes = ['Steve', 'Bill', 'Martin']
literatura = [8.5, 9, 10]
matematica = [9, 9.5, 7]

dict1 = {'nomes': nomes, 'literatura': literatura, 'matematica': matematica}

df1 = pd.DataFrame(dict1)

print(df1)

df2 = pd.DataFrame([literatura, matematica], columns=nomes)

print(df2)

print(df2.describe())

a = np.random.random(50)

# plt.plot(a, 'ro')

# plt.boxplot(a)

plt.plot(a)


plt.show()