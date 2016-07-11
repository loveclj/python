#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: np_process.py
@time: 6/29/16 4:44 PM
"""


import codecs
import nltk
import re


def lemmatize_noun_phrase(infile, outfile):

    lemmatize = nltk.stem.WordNetLemmatizer().lemmatize
    pattern = re.compile(r'[a-zA-Z][a-zA-Z0-9-/ ]+$')
    with codecs.open(filename=infile, mode="r", encoding='utf-8') as infd, codecs.open(filename=outfile, mode="w", encoding='utf-8') as  outfd:
        while True:
            line = infd.readline().strip('\n')

            if not line:
                break

            pid, phrases = line.split(':')

            phrase_list = phrases.split(',')
            phrase_lemm_list = []

            for phrase in phrase_list:
                if not pattern.match(phrase):
                    continue

                if len(phrase) < 4:
                    continue

                words = phrase.strip().split(' ')
                if len(words) > 3:
                    continue

                words[-1] = lemmatize(words[-1])
                phrase_lemm = u" ".join(words)
                if phrase_lemm != phrase:
                    print phrase_lemm
                    print phrase
                phrase_lemm_list.append(phrase_lemm)

            line = pid + ":" + u",".join(phrase_lemm_list) + '\n'
            outfd.write(line)

if __name__ == '__main__':

    infilename = './pid2nps.text'
    outfilename = "./pid2processed_nps.text"
    lemmatize_noun_phrase(infilename, outfilename)