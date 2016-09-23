#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: simple_linear_regression.py
@time: 9/9/16 10:20 AM
"""

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

X = [[1], [2], [5], [10]]
Y = [[2], [4], [7], [15]]

model = LinearRegression()
model.fit(X, Y)


alpha = model.coef_[0][0]
beta = model.intercept_[0]

LineX = np.arange(20)  # list multiby a scalar  will expand list
LineY = LineX * alpha + beta  # not every element of list multiply this scalar




plt.figure()
plt.xlabel("X")
plt.ylabel("Y")

plt.plot(X, Y, 'k.')
plt.plot(LineX, LineY)

plt.axis([0, 20, 0, 20])
plt.grid(True)

plt.show()