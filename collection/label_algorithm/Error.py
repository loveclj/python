#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: Error.py
@time: 3/21/16 3:57 PM
"""


class Error(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


if __name__ == '__main__':
    pass