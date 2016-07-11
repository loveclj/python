#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: term_frequence.py
@time: 3/21/16 5:03 PM
"""

import snowballstemmer

from nltk.corpus import stopwords
from string_utility import split_text


def get_stem_freq(words_list, stem2term, lang):

    porterStemWord = snowballstemmer.PorterStemmer().stemWord

    stop_words = ""
    if lang == "EN":

        # stop_words = stopwords.words('english')
        fd = open("stopwords", "r")
        stop_words_list = []
        for line in fd.readlines():
            word = line.strip('\n').decode('utf-8')
            stop_words_list.append(word)

        stop_words_set = set(stop_words_list)

    stem_freq = {}

    for word in words_list:
        stem = porterStemWord(word)

        if stem in stop_words_set:
            print "filter", stem
            continue
        else:
            print stem
            stem2term[stem] = word
            if stem in stem_freq.keys():
                stem_freq[stem] += 1
            else:
                stem_freq[stem] = 1

    return stem_freq



if __name__ == '__main__':
    pass