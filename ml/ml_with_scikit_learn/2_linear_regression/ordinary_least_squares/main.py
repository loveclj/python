#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: main.py
@time: 9/8/16 5:17 PM
"""


from sklearn import linear_model
import numpy as np


if __name__ == '__main__':
    data = [[1, 1], [2, 2], [3, 3]]  # 2 D (x, y)
    target = [0, 1, 3]  # z
    clf = linear_model.LinearRegression()
    clf.fit(data, target)  # find z = ax + by + c

    print clf.coef_
    print clf.intercept_

    data = np.array(data)
    print data[:, :, np.newaxis,np.newaxis].shape
