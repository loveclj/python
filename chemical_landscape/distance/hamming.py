#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: hamming.py
@time: 7/14/16 1:30 PM
"""

def hamming_distance(v1, v2):

    dimession = len(v1)
    d = 0
    for i in range(dimession):
        if v1[i] != v2[i]:
            d += 1

    return d



if __name__ == '__main__':
    pass