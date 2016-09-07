#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: index_trick.py
@time: 9/7/16 4:44 PM
"""

import numpy as np


a = np.arange(12)
print a.reshape( [2, -1, 3] )  # -1 means whatever is needed
