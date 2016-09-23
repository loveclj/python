#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: tf_idf_vector.py
@time: 9/23/16 12:33 PM
"""

from sklearn.feature_extraction.text import TfidfVectorizer

corpus = ['the dog ate a sandwich and I ate a sandwich',
          'the wizard transfigured a sandwich']

vectorizer = TfidfVectorizer(stop_words='english')

print vectorizer.fit_transform(corpus).todense()

if __name__ == '__main__':
    pass