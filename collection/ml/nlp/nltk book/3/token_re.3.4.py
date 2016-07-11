#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: token_re.3.4.py.py
@time: 1/26/16 5:02 PM
"""
from nltk.corpus import gutenberg, nps_chat
import nltk

if __name__ == '__main__':
    moby = nltk.Text(gutenberg.words("melville-moby_dick.txt"))

    # very important!!!!
    # <>means a word
    print moby.findall(r"<a> (<.*>) <man>")