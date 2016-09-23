#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: polynomial.py
@time: 9/9/16 1:56 PM
"""

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import numpy as np
import matplotlib.pyplot as plt

x = [[1], [2], [3], [4], [5]]
y = [[1], [4], [9], [16], [20]]
x = np.array(x)
y = np.array(y)
x_linspace = np.linspace(start=0, stop=15, num=100).reshape(-1, 1)

line_model = LinearRegression()
line_model.fit(x, y)
y_line_predict = line_model.predict(x_linspace)

poly_model = PolynomialFeatures(degree=2)
x_train_quadratic = poly_model.fit_transform(x)
x_linspace_quadratic = poly_model.transform(x_linspace)

poly_regression = LinearRegression()
poly_regression.fit(x_train_quadratic, y)

y_poly_predict = poly_regression.predict(x_linspace_quadratic)
print y_poly_predict

plt.figure()
plt.axis([0, 20, 0, 50])
plt.plot(x.reshape(-1), y.reshape(-1), 'k.')
print x.reshape(1, -1)
plt.plot(x_linspace.reshape(-1), y_line_predict.reshape(-1))
plt.plot(x_linspace.reshape(-1), y_poly_predict.reshape(-1))

# print x_linspace.reshape(1, -1)
plt.show()








