#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: copy_deep_copy.py
@time: 9/7/16 3:08 PM
"""

import numpy as np


''' no copy '''
a = np.arange(12)
b = a
print a is b  # no copy, a is same as b

b.shape = 3, 4
print a.shape  # shape of a is changed when shape of b is changed
print id(a), id(b)  # ids are same

print '===================='


''' view, or shallow copy '''

a = np.arange(12)
b = a.view()
print a is b  # a is not same as b
print id(a), id(b)  # ids are not same

b.shape = 3, 4
print a.shape  # shape of a is not changed when shape of b is changed

print b.base is a  # b is view of the data owned by a

print b.flags.owndata  # b doesn't own data

b[0, 3] = -1
print a  # data is changed

print "=============="


''' deep copy '''

a = np.arange(12)
b = a.copy()

print a is b  # ids are not same

print b.base is a  # b is not view of data owned by a

b[4] = -1
print a  # a is not changed