#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: multiple_linear_regression.py
@time: 9/9/16 1:50 PM
"""


import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

X = [[1, 2], [2, 4], [5, 7], [10, 12]]
Y = [[2], [4], [7], [15]]

test_X = np.random.random(size=[10, 2])
print test_X

model = LinearRegression()
model.fit(X, Y)

print model.predict(test_X)

print model.coef_
print model.intercept_


