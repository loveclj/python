#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: count_vector.py
@time: 9/23/16 11:05 AM
"""

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import euclidean_distances

corpus = ['dog likes to eat meat',
          'cat likes to eat fish']

vectorizer = CountVectorizer(stop_words='english')

print vectorizer.fit_transform(corpus).todense()
print vectorizer.fit_transform(corpus).toarray()
print vectorizer.vocabulary_

matrix = vectorizer.fit_transform(corpus).toarray()

print euclidean_distances(matrix[0], matrix[1])
print euclidean_distances(matrix)  # distance matrix

if __name__ == '__main__':
    pass