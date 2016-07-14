#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: decorator.py
@time: 7/13/16 4:34 PM
"""


def decorator(fun):
    def wrapper(*args, **kvargs):
        print "decorateor"
        print args
        print kvargs

        fun(*args, **kvargs)

    return wrapper


@decorator
def fun(a, b, c=1):

    print "fun"
    print a
    print b
    print c


if __name__ == '__main__':
    fun(1, 2,4)