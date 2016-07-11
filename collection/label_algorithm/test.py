#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: test.py.py
@time: 3/22/16 6:18 PM
"""

if __name__ == '__main__':

        fd = open("stopwords", "r")
        words_list = []
        for line in fd.readlines():
            word = line.strip('\n').decode('utf-8')

            words_list.append(word)

        stop_words = set(words_list)
        print stop_words