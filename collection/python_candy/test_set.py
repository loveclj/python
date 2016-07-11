#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: test_set.py.py
@time: 3/25/16 2:46 PM
"""
# https://docs.python.org/2/library/stdtypes.html#set-types-set-frozenset

a = set("adfs")
print a

b = set(range(10))
print b

c = a.union(b)
print c

print a & b
print a - b
print a ^ b
print a | b







if __name__ == '__main__':
    pass