#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: matrix_basic_operation.py
@time: 9/7/16 2:01 PM
"""

import numpy as np

A = np.array(np.arange(10)).reshape(2, 5)
print A

B = A.reshape(5, 2)
print B

print A.dot(B)  # matrix product


C = B.transpose()
print C

print A * C  # elementwise product


print A.sum()
print A.min()
print A.max()

print A.sum(axis=1)  # add by row
print A.sum(axis=0)  # add by col

print A.cumsum(axis=1)
print A

print np.exp(A)
print np.sqrt(A)
print np.add(A, A)
print A * 2


