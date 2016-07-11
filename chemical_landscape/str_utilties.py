#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: str_utilties.py
@time: 7/5/16 6:37 PM
"""

import nltk
import StringIO
import gzip
import re
import enchant
import nltk.corpus
import base64
import gzip
import binascii


def binary2string(encode):
    obj = StringIO.StringIO(encode)
    gzip_obj = gzip.GzipFile(fileobj=obj)
    decode = gzip_obj.read()
    gzip_obj.close()
    return decode


def gzipstring(raw):
    out = StringIO.StringIO()
    with gzip.GzipFile(fileobj=out, mode="w") as f:
        f.write(raw)

    return out.getvalue()

    return s


def char2binary(c):
    b = bin(c)[2:]
    b = '0' * (8 - len(b)) + b
    return b


def str2binary(s, binary_begin=32, binary_end=-7):
    binary_list = map(char2binary, bytearray(s))
    binary = "".join(binary_list)[binary_begin: binary_end]
    return binary


if __name__ == '__main__':
    base64_str = "AAADceB7sABAAAAAAAAAAAAAAAAAAeLECAAwAAAAAAAWAAAB8AAAHgQICAAADIzB3wQzl5cIEgiuAydydACS9KthKLgdmDW+TJiIbrLi2ROU8AhszhPImCe4yBAOAAABAAAAAAAAAAIAAAAAAAAAAAAAAA=="

    base64_str2 = "AAADcYBzAQBEAAAAAAAAAAAAAAAAAAAAAAAsWAAAAAAAAAAB4AAAHQYAAAAACADBUgw9kZYIEAigADBnZACC0ClxCrAJ2Dg4ZJiIKOLg2dGEJAxogALoyCYQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=="

    decode = base64.decodestring(base64_str)

    b = str2binary(decode)
    print b
    print len(b)

    decode = base64.decodestring(base64_str2)

    b = str2binary(decode)
    print b
    print len(b)