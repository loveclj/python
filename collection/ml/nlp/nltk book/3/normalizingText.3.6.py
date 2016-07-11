#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: normalizingText.3.6.py.py
@time: 1/26/16 5:07 PM
"""

import nltk


if __name__ == '__main__':

    raw = """DENNIS: Listen, strange women lying in ponds distributing swords
     is no basis for a system of government.  Supreme executive power derives from
      a mandate from the masses, not from some farcical aquatic ceremony."""

    tokens = nltk.word_tokenize(raw)
    porter = nltk.PorterStemmer()
    lancaster = nltk.LancasterStemmer()

    porter_stem = [porter.stem(token) for token in tokens]
    land_stem = [lancaster.stem(token) for token in tokens]

    print porter_stem
    print land_stem
