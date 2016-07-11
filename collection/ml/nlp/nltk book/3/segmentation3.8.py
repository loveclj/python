#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: segmentation3.8.py.py
@time: 1/26/16 5:23 PM
"""

from __future__ import division
import nltk



if __name__ == '__main__':
    print len(nltk.corpus.brown.words()) / len(nltk.corpus.brown.sents())
    text = nltk.corpus.gutenberg.raw('chesterton-thursday.txt')
    sents = nltk.sent_tokenize(text)
    print sents[1]