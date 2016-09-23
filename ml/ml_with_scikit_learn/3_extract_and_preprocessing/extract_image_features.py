#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: extract_image_features.py
@time: 9/23/16 1:44 PM
"""
from sklearn import datasets

digits = datasets.load_digits()
print 'Digit:', digits.target[0]
print digits.images[0].reshape(-1, 64)
if __name__ == '__main__':
    pass