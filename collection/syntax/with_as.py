#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: with_as.py.py
@time: 1/26/16 1:52 PM
"""

class Divide:
    def __init__(self, n):
        self.n = n

    def __enter__(self):
        return self

    def divide(self):
        return float(10)/self.n

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print exc_val
            print exc_tb
            return False


if __name__ == '__main__':
    try:
        with Divide(0) as a:
            print a.divide()
    except:
         print "error"

    with open("xxx", 'r') as f:
        buf = f.read()