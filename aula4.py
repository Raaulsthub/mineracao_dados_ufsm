import numpy as np 
import pandas as pd 
from matplotlib import pyplot as plt
from sklearn import linear_model
from sklearn.linear_model import LinearRegression

a = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]).reshape(-1, 1)
b = np.array([3, 5, 10, 20, 30, 100, 120, 130, 140, 150]).reshape(-1, 1)

model = LinearRegression()
model.fit(a, b)

i = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]).reshape(-1, 1)

linear_model = model.predict(i)

print(linear_model)


