#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: utility.py
@time: 3/21/16 3:21 PM
"""

import re


def split_text(doc):
    # splitter = re.compile('\\W*')
    splitter = re.compile(r'[^a-zA-Z-]*')
    words = [s.lower() for s in splitter.split(doc) if len(s) > 2 and len(s) < 20]
    return words


if __name__ == '__main__':
    doc = "dog sex, cat..  bird?     man cat ?"
    print split_text(doc)