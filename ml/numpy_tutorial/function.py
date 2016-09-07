#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: function.py
@time: 9/7/16 2:24 PM
"""

import numpy as np


def f(x, y):
    return 10*x + y

A = np.fromfunction(f, (4, 5), dtype='int64')
print A

a = A[:, 0]
b = A[0, :]
print a
print b

print a.shape
print b.shape



