#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: hash_vector.py
@time: 9/23/16 1:37 PM
"""
from sklearn.feature_extraction.text import HashingVectorizer

corpus = ['the', 'cat', 'bacon', 'ate']

vectorizer = HashingVectorizer(n_features=6)
print vectorizer.fit_transform(corpus).todense()



if __name__ == '__main__':
    pass