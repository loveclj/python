#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: line_algebra.py
@time: 9/7/16 4:29 PM
"""

import numpy as np


# np.set_printoptions(precision=1)

print np.eye(3)  # identity matrix

a = np.random.random(size=(4, 4))
print a

print a.trace()  # trace of matrix a

inverse_a = np.linalg.inv(a)  # inverse matrix
print np.dot(a, inverse_a)

y = np.random.random(size=(4, 1))

print np.linalg.solve(a, y)  # solve ax = y

print np.linalg.eigvals(a)  # eigenvalue of matrix a
print np.linalg.eig(a)  # eigenvalue and eigenvector of matrix a

