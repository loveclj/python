#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: test.py
@time: 4/14/16 5:38 PM
"""
import nltk
import time
if __name__ == '__main__':


    start = time.time()
    fd = open("../title", "r")
    lines = fd.readlines()
    count = len(lines)/2

    for j in range(10):

        for i in range(count):
            setente = lines[2*i+1].strip('\n')
            token = nltk.word_tokenize(setente.lower())
            print nltk.pos_tag(token)

    print count
    print time.time() - start