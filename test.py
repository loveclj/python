#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: test.py.py
@time: 1/27/16 2:18 PM
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


def c2binary(c):
    b = bin(c)[2:]
    s = '0' * (8 - len(b))+ b
    return s

# ss= "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"
# ss = "H4sIAAAAAAAAAHs+c+/L1klA9Hzytvd7Op7s6nm/pxMAvuVndxUAAAA="
#
#
# pid = "d8b5f389-f3c1-4cb0-a181-045df2d2a5c4"
# ss= "H4sIAAAAAAAAAA3DgQnAIAwEwFUyUlcI5rUB68vH7t8e3CU2VFmnbAvblWtYZDUG9HBmwHzF3yfHi7JzQ2D/ALVzHVs6AAAA"
# s = base64.decodestring(ss)
# print binary2string(s)

# ss = base64.decodestring(ss)
#
# print ss

#
# print decode

# print nltk.PorterStemmer().stem_word("more")
# print nltk.stem.WordNetLemmatizer().lemmatize("more")

# w = "hello1ww"
#
# mode = r'[a-zA-Z-]+$'
#
# pattern = re.compile(mode)
# print pattern.match(w)
#
# a = set()
# a.add("a")
# a.add("b")
# print sorted(a)


ss = "AAADceB7sABAAAAAAAAAAAAAAAAAAeLECAAwAAAAAAAWAAAB8AAAHgQICAAADIzB3wQzl5cIEgiuAydydACS9KthKLgdmDW+TJiIbrLi2ROU8AhszhPImCe4yBAOAAABAAAAAAAAAAIAAAAAAAAAAAAAAA=="
#
ss = "AAADceByOAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHgAAAAAACBThgAYCCAMABAAIAACQCAAAAAAAAAAAAAEIAAACABQAgAAHAAAFIAAQAAAkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=="
ss = "AAADcfB/OAAAAAAAAAAAAAAAGDAAAQAAAAAgQAAAAAAAAACAAAAAHgAACAAADzzhgAYDCAMABgCoAiPyPAAAAAEgAAAJCAE4AAgIEBYAiQAGQAAH5gCIgAOY3PLPgAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=="

# print  binary2string(decode)
decode = base64.decodestring(ss)
# print len(decode)
# print type(decode)
# print decode


fingerprint_list = map(c2binary, bytearray(decode))
# print fingerprint_list
fingerprint = "".join(fingerprint_list)[32:-7]
print fingerprint
# print len(fingerprint)
# x = bytearray(decode)
# print len(x)
# for i in x:
#     print i,



# print binascii.b2a_hex(decode)
#
# i = 0
# for d in decode:
#     n = binascii.b2a_hex(d)
#     print n
#     print int(n, 16)
#     i += 1
    # print i
# print binary2string(decode)