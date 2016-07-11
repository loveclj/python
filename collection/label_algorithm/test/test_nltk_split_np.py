#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: test_nltk_split_np.py
@time: 3/23/16 5:50 PM
"""

import nltk
import re
import pprint
#
# def ie_preprocess(document):
#     sentences = nltk.sent_tokenize(document)
#     sentences = [nltk.word_tokenize(sent) for sent in sentences]
#     sentences = [nltk.pos_tag(sent) for sent in sentences]
#     return sentences
#
# if __name__ == '__main__':
#     mystr = 'Data center cooling system'
#     sentences = ie_preprocess(mystr)
#     grammar = "NP: {<PRP|PRP\$><.*>*<NN|NNP>}"
#     cp = nltk.RegexpParser(grammar)
#     for sentence in sentences:
#         result = cp.parse(sentence)
#         print result

text = "data center cooling system"
sentence = nltk.word_tokenize(text)
print sentence
sentence = nltk.pos_tag(sentence)
print sentence

grammar = "NP: {<DT>?<JJ>*<NN>}"
cp = nltk.RegexpParser(grammar)
result = cp.parse(sentence)
print result
