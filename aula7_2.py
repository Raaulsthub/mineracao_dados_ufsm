import numpy as np
import pandas as pd

matrix = np.zeros((10, 10), dtype=int)

conta = 0

for i in range(10):
    conta += 1
    matrix[i, i] = conta


print(matrix)

vector = []

for i in range(10):
    for j in range(10):
        if matrix[i, j] != 0:
            vector.append(matrix[i, j])

print(vector)