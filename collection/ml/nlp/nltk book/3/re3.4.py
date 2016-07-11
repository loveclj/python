#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: re3.4.py.py
@time: 1/26/16 4:48 PM
"""
import nltk
import re

if __name__ == '__main__':
    pattern = re.compile("ed$")
    for w in nltk.corpus.words.words("en"):
        if pattern.search(w):
            print w

    pattern = re.compile("^[abc][def][ghi]$")
    for w in nltk.corpus.words.words("en"):
        if pattern.search(w):
            print w


    pattern