#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: standardization.py
@time: 9/23/16 1:50 PM
"""
from sklearn import preprocessing
import numpy as np

X = np.random.random(size=(5, 5))
print X
print preprocessing.scale(X)  # standardization
if __name__ == '__main__':
    pass