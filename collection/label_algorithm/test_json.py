#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: test_json.py.py
@time: 3/22/16 4:12 PM
"""
import json


if __name__ == '__main__':
    fd = open("label_keywords_topk20", 'r')
    label = json.load(fd)
    print label