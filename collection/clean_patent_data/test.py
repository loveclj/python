#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: test.py.py
@time: 6/2/16 6:19 PM
"""

import nltk
import langid
import codecs

def  detect_language(filename):
    with codecs.open(filename=filename, mode="r", encoding="utf-8") as fd:
        while True:
            line = fd.readline().strip("\n")
            print line
            if not line:
                break
            title = line.split(':')[1]
            print langid.classify(title), ":", title

if __name__ == '__main__':
    print hex(ord(u'é'))
    detect_language("../data/fail_pid2title.text")


   # e as¹bactericides