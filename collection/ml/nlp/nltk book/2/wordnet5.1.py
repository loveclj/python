#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: wordnet5.1.py.py
@time: 1/26/16 2:25 PM
"""
from nltk.corpus import wordnet as wn

if __name__ == '__main__':
    s = wn.synsets('motorcar')
    print s

    lemma = wn.synset('car.n.01').lemma_names()
    print lemma

    print wn.synset('car.n.01').definition()
    print wn.synset('car.n.01').examples()

    print wn.synset('car.n.01').lemmas()

    print wn.synsets('car')