#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: data_structure.py
@time: 9/9/16 5:02 PM
"""
import pandas as pd
import numpy as np

s = pd.Series([1, 2, 's', True])  # Series can store different type
print s

dates = pd.date_range('20160203', periods=6)
dates = pd.date_range('20160203', periods=6, freq='M')  # time series

df = pd.DataFrame(np.random.random(size=(6, 4) ), index=dates, columns=list('ABCD'))
print df

print dates
if __name__ == '__main__':
    pass