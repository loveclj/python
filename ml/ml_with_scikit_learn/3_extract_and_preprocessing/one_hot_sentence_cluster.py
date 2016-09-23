#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: one_hot_sentence_cluster.py
@time: 9/23/16 11:20 AM
"""
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import euclidean_distances
from nltk.stem.wordnet import WordNetLemmatizer


text = '''Trump's heart-tugging words about Root were reminiscent of
his interest in the slaying of Kate Steinle, the 32-year-old woman
who was killed by a stray bullet at a San Francisco pier in July 2015.
 Steinle's killer was an undocumented citizen who had been deported
 five times by the federal government, but was remaining in
  San Francisco, which is also a sanctuary city. Trump capitalized on
   Steinle's death to advocate for his draconian anti-immigration
   platform last summer; now, it seems, he has moved onto Sarah Root
   and her grieving family.'''

if __name__ == '__main__':
    sentences = text.split(',')
    print sentences
    countVectorizer = CountVectorizer(stop_words='english')
    matrix = countVectorizer.fit_transform(sentences).toarray()
    print countVectorizer.vocabulary_
    print euclidean_distances(matrix)

    lemmatizer = WordNetLemmatizer()
    print lemmatizer.lemmatize('clustering', 'v')
    print lemmatizer.lemmatize('clustering', 'n')

    print countVectorizer.fit_transform([text]).toarray()
    print countVectorizer.vocabulary_