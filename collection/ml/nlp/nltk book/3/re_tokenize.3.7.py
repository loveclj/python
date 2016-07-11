#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: re_tokenize.3.7.py.py
@time: 1/26/16 5:15 PM
"""
import nltk
import re


if __name__ == '__main__':
    raw = """DENNIS: Listen, strange women lying in ponds distributing swords
     is no basis for a system of government.  Supreme executive power derives from
      a mandate from the masses, not from some farcical aquatic ceremony."""

    # split by space, Tab or enter
    print re.split(r'[ \t\n]', raw)

    # \w means word characters, equivalent to [a-zA-Z0-9_]
    # \W means all characters other than letters, digits or underscore
    print re.split(r'\W+', raw)