#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: merge.py
@time: 3/30/16 11:45 AM
"""
import re


def load_stopwords_from_file(filename):
    fd = open(filename, "r")
    stopwords = []

    pattern = re.compile(' |\t')

    for line in fd.readlines():

        line = line.strip('\n')
        words = pattern.split(line)

        stopwords.extend(words)

    fd.close()

    return set(stopwords)


def get_difference_set(set1, set2):

    difference_set = []
    for word in set2:
        if word not in set1:
            difference_set.append(word)

    return difference_set


def add_stopswords_by_file(stopword_file1, stopword_file2, stopword_file_collection):
    stopwords1 = load_stopwords_from_file(stopword_file1)
    stopwords2 = load_stopwords_from_file(stopword_file2)

    stopwords_collection = stopwords1.union(stopwords2)

    fd = open(stopword_file_collection, "w")
    for word in stopwords_collection:
        if word:
            fd.write(word + '\n')

    fd.close()




if __name__ == '__main__':
    uspto_stopwords = load_stopwords_from_file("uspto_stopwords.text")
    print uspto_stopwords
    stopwords = load_stopwords_from_file("../stopwords")
    print stopwords

    add_stopswords_by_file("../stopwords", "uspto_stopwords.text", "stopwords_update.text")
