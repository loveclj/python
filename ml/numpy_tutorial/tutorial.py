#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: tutorial.py
@time: 9/7/16 1:35 PM
"""


import numpy as np


''' array is alias of ndarray '''

''' method and member of ndarray '''

a = np.arange(20).reshape(4, 5)

print a.shape
print a.ndim
print a.size
print a.dtype
print a.itemsize
print a.data
print type(a)

c = np.array([[1, 2], [3, 4] ], dtype='complex')
print c.conjugate()
print np.zeros([2, 3])
print np.empty(shape=(2, 4), dtype='complex64')

print np.arange(start=1, stop=10, step=1, dtype='int32')

x = np.linspace(start=0, stop=2*np.pi, num=5)
print x
print np.sin(x)

np.set_printoptions(precision=2, threshold=5)
print x

print x ** 2

print np.random.random( size=(2, 3) )

print x.dtype