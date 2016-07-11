#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: filter_meaningless_words.py
@time: 5/13/16 1:08 PM
"""

import codecs
import re

def filter_meaningless_words(inputfile, outputfile):

    i = 0
    infd = codecs.open(inputfile, "r", 'utf-8')
    outfd = codecs.open(outputfile, "w", "utf-8")

    mode = re.compile(r'\d+')

    while True:
        line = infd.readline()

        if not line:
            break

        kv = line.strip('\n').split(":")

        if len(kv[0]) > 6:
            print kv[0]
            continue

        if mode.findall(kv[0]):
            i += 1
        else:
            outfd.write(line)
    print i

    infd.close()
    outfd.close()


if __name__ == '__main__':

    filter_meaningless_words("cn_word_freq.text", "cn_word_freq_filtered.text")