#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: merge_matrix.py
@time: 9/7/16 2:52 PM
"""

import numpy as np

a = np.random.random((2, 3))
b = np.random.random((2, 3))
print a
print b

print np.vstack((a, b))
print np.hstack((a, b)).T

print ''' ------ column_stack '''

a = np.array([1, 2])
b = np.array([3, 4])

print a[:, np.newaxis]  # newaxis allow to have a 2D columns vector
print np.column_stack((a[:, np.newaxis], b[:, np.newaxis]))
print np.hstack((a[:, np.newaxis], b[:, np.newaxis]))
