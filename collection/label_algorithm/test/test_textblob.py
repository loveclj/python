#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: test_textblob.py
@time: 4/14/16 10:43 AM
"""
import time
from textblob import TextBlob

text = "System for remotely controlling device of node featuring " \
       "client application that displays virtual component " \
       "corresponding to physical component of device and remote site " \
       "located remote from node for sending control commands received from" \
       " client application to node"

text = "data center cooling system"

start = time.time()
blob = TextBlob(text)
print blob.tags           # [('The', 'DT'), ('titular', 'JJ'),
                    #  ('threat', 'NN'), ('of', 'IN'), ...]

# print blob.noun_phrases   # WordList(['titular threat', 'blob',
                    #            'ultimate movie monster',
                    #            'amoeba-like mass', ...])
print time.time() - start
for sentence in blob.sentences:
    print(sentence.sentiment.polarity)
# 0.060
# -0.341

blob.translate(to="es")  # 'La amenaza titular de The Blob...'
