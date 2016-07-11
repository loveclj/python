#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: probability_func.py.py
@time: 1/27/16 1:44 PM
"""
import scipy
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    n = 10
    p = 0.4
    k = np.arange(0, 12)
    binomial = stats.binom.pmf(k, n, p)
    plt.plot(k, binomial)
    plt.show()
