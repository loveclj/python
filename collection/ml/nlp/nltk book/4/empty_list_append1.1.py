#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: empty_list_append1.1.py.py
@time: 1/26/16 5:58 PM
"""

if __name__ == '__main__':
    empty = []

    # empty in list is just shallow copy
    nested = [empty, empty, empty]
    # This is because each of the three elements is actually just a reference to one and the same list in memory.
    empty.append("python")
    print nested

    a = [[]] * 3
    a[1].append("a")
    a[1] = "b"
    print a

    # why?
    n1 = 2
    n2 = 2
    print n1 is n2  # true
    list1 = []
    list2 = []
    print list1 is list2  # false
