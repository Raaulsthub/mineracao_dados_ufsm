import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.linear_model import SGDOneClassSVM
from sklearn.ensemble import AdaBoostClassifier
from sklearn.neural_network import MLPClassifier


from sklearn import datasets 

X, y = datasets.load_iris( return_X_y = True)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.30)


# RANDOM FOREST
model_rf = RandomForestClassifier(n_estimators=100)
model_rf.fit(X_train, y_train)
y_pred = model_rf.predict(X_test)

print("ACCURACY OF THE RANDOM FOREST (100 ESTIMATORS) MODEL: ", metrics.accuracy_score(y_test, y_pred))

# SUPPORT VECTOR MACHINE
model_svm = svm.SVC()
model_svm.fit(X_train, y_train)
y_pred_2 = model_svm.predict(X_test)

print("ACCURACY OF THE SUPPORT VECTOR MACHINE MODEL: ", metrics.accuracy_score(y_test, y_pred_2))

# LINEAR REGRESISON MODEL

model_lr = SGDOneClassSVM()
model_lr.fit(X_train, y_train)
y_pred_3 = model_lr.predict(X_test)

# print(y_pred_3, end='\n\n')
# print(y_test)

print("ACCURACY OF THE LINEAR SGD MODEL: ", metrics.accuracy_score(y_test, y_pred_3))

# ADA BOOST MODEL

model_adaBoost = AdaBoostClassifier()
model_adaBoost.fit(X_train, y_train)
y_pred_4 = model_adaBoost.predict(X_test)

print("ACCURACY OF THE ADABOOST MODEL MODEL: ", metrics.accuracy_score(y_test, y_pred_4))

# 3 LAYERS PERCEPTRON

clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(100, 3), random_state=1)
clf.fit(X_train, y_train)
y_pred_5 = clf.predict(X_test)

print("ACCURACY OF 3 LAYERS (100 NEURONS) PERCEPTRON: ", metrics.accuracy_score(y_test, y_pred_5))

