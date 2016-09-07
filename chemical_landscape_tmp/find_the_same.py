#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: find_the_same.py.py
@time: 8/1/16 3:41 PM
"""

if __name__ == '__main__':
    l = []
    for line in open("./formula_figerprint_ali_suger_data.text"):
        l.append(line.strip('\n').split(',')[1])


    length = len(l)

    for i in range(length-1):
        for j in range(i+1, length):
            print i, j, l[i] == l[j]

