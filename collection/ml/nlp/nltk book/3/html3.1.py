#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: html3.1.py.py
@time: 1/26/16 3:31 PM
"""

import urllib
import nltk
from bs4 import BeautifulSoup



if __name__ == '__main__':
    url = "http://news.bbc.co.uk/2/hi/health/2284783.stm"
    html = urllib.urlopen(url).read().decode('utf-8')
    # print html
    raw = BeautifulSoup(html).get_text()
    tokens = nltk.word_tokenize(raw)
    # print tokens
    text = nltk.Text(tokens)
    concordance = text.concordance('gene')
    print concordance