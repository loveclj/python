#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: shape.py
@time: 9/7/16 2:38 PM
"""

import numpy as np


A = np.floor(np.random.random(size=(4, 3)) * 10)
print A

b = A.ravel()  # flatten the array
print b
print b.shape
print A.shape


''' reshape vs resize '''
print '''---------shape resize '''

C = np.random.random(size=(2, 4))
print C.shape
print C.reshape(4, 2).shape  # not change C
print C.shape
print C.resize(4, 2)  # change C, return None
print C.shape
