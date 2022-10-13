from operator import indexOf
import numpy as np
import pandas as pd

def find_index(find, list):
    a = 0
    for i in list:
        if i == find:
            return a
        a += 1
    return -1

df = pd.read_csv('./data/z.csv')

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

print('\n\n')
print(find_index('C', alphabet))

matrix = df.to_numpy()

print(matrix)

a = np.zeros((5, 26))

for i in range(5):
    for j in range(5):
        a[i, find_index(matrix[i, j], alphabet)] = 1

print(a)

for i in alphabet:
    print(i)
