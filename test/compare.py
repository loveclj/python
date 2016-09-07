#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: compare.py
@time: 9/1/16 12:53 PM
"""


if __name__ == '__main__':
    fd1 = open('t', 'r')
    fd2 = open('tt', 'r')

    c = 0

    for i in range(88100):
        a = eval(fd1.readline().strip('\n'))
        b = eval(fd2.readline().strip('\n'))

        if abs(a -b) > 0.1:
            print i, a, b
            c += 1

    print c
