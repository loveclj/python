#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: split.py
@time: 9/7/16 3:05 PM
"""

import numpy as np

A = np.random.random(size=(4, 6))
print A

print np.hsplit(ary=A, indices_or_sections=3)
print np.vsplit(ary=A, indices_or_sections=2)
