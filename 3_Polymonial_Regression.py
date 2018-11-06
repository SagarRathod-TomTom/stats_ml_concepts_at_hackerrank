"""
Problem Statement:
https://www.hackerrank.com/challenges/predicting-office-space-price/problem

Useful Link:
https://www.coursera.org/learn/machine-learning/supplement/bjjZW/normal-equation

"""

# Python Code solved using Normal Equation
import numpy as np

F, N = map(int, input().split(' '))
training_data = []

for i in range(N):
    row = list(map(float, input().split(' ')))
    training_data.append(row)

T = int(input())
test_data = []
for t in range(T):
    row = list(map(float, input().split(' ')))
    test_data.append(row)

training_data = np.array(training_data, dtype=np.float32)
test_data = np.array(test_data, dtype=np.float32)

trainX = training_data[:, 0:F]
trainY = training_data[:, F].reshape(-1, 1)


def transform_into_poly_features(arr):
    m, n = arr.shape
    for i in range(n):

        if i == 4:
            i = 3
        arr[:, i] = arr[:, i] ** (i + 1)
    return arr


trainX = transform_into_poly_features(trainX)
ones = np.ones((trainX.shape[0], 1))
trainX = np.hstack((ones, trainX))

# Normal Equation
transpose_trainX = np.transpose(trainX)
theta = np.dot(np.dot(np.linalg.pinv(np.dot(transpose_trainX, trainX)), transpose_trainX), trainY)

test_data = transform_into_poly_features(test_data)
test_data = np.hstack((np.ones((test_data.shape[0], 1)), test_data))
preds = np.dot(np.transpose(theta), np.transpose(test_data))

for i in range(preds.shape[1]):
    print('%.3f' % preds[0, i])


#Code Solution using sklearn library

import numpy as np
from sklearn import linear_model as lm
from sklearn import preprocessing as pp

F, N = map(int, input().split())
train = np.array([input().split() for _ in range(N)], float)
T = int(input())
test = np.array([input().split() for _ in range(T)], float)

mod = lm.LinearRegression()
XtoP = pp.PolynomialFeatures(3, include_bias=False)
mod.fit(XtoP.fit_transform(train[:, :-1]), train[:, -1])

ymod = mod.predict(XtoP.fit_transform(test))
print(*ymod, sep='\n')