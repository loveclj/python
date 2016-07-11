#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: gzip_api.py
@time: 3/21/16 1:33 PM
"""

import StringIO
import gzip


def decompress(encode):
    obj = StringIO.StringIO(encode)
    gzip_obj = gzip.GzipFile(fileobj=obj)
    decode = gzip_obj.read()
    gzip_obj.close()
    return decode


def compress(raw):
    out = StringIO.StringIO()
    with gzip.GzipFile(fileobj=out, mode="w") as f:
        f.write(raw)

    return out.getvalue()


if __name__ == '__main__':

    raw_str = "hello, compress"
    compress_str = compress(raw_str)
    decompress_str = decompress(compress_str)
    print "raw str is :", raw_str
    print "compress str is:", compress_str
    print "decompress str is:", decompress_str
