#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: __init__.py.py
@time: 6/2/16 11:56 AM
"""

import codecs
import re

fail_title_path = "../data/fail_pid2title.text"

''' char unknown '''
UNKNOWN = 0

FULL_WIDTH_CHAR = 10

''' half with char '''
HALF_WIDTH_CHAR = 20
NUMBER = 21
UPPER_CASE_CHAR = 22
LOWER_CASE_CHAR = 23
PUNCTUATION = 24

''' illegal char '''
ILLEGAL_CHAR = 30
CHINESE_DOUBLE_QUOTATION = 31
CHINESE_SINGLE_QUOTATION = 32

''' control and basic latin '''
CONTROL_CHAR = 40

''' Dashes, connection number, hyphen, minus '''
DASH = 50

''' Superscript or Subscript'''
SCRIPT = 60


if __name__ == '__main__':
    pass