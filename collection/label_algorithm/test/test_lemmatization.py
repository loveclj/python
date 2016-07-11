#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: test_lemmatization.py.py
@time: 3/23/16 5:20 PM
"""


import nltk

lemmatize = nltk.stem.WordNetLemmatizer().lemmatize

if __name__ == '__main__':
    print lemmatize("dogs")
    print lemmatize("loving")
    print lemmatize("aardwolves")
