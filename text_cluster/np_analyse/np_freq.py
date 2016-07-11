#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: np_freq.py
@time: 6/29/16 5:40 PM
"""


import codecs
import fileIO


def get_phrase_freq(infile):
    phrase_set = set()
    phrase_freq = {}
    with codecs.open(filename=infile, mode="r", encoding='utf-8') as infd:

        while True:
            line = infd.readline().strip('\n')

            if not line:
                break

            pid, phrase_str = line.split(':')
            phrase_list = phrase_str.split(',')
            for phrase in phrase_list:
                if phrase in phrase_set:
                    phrase_freq[phrase] += 1
                else:
                    phrase_set.add(phrase)
                    phrase_freq[phrase] = 1

    return phrase_freq


def compare_kv(a, b):
    return eval(a[-1]) - eval(b[-1])
if __name__ == '__main__':
    # infile = "./pid2processed_nps.text"
    outfile = "./phrase_freq.text"
    # phrase_freq = get_phrase_freq(infile)
    # fileIO.dumps.dump_map_to_file(filename=outfile, dic=phrase_freq)
    phrase_freq = fileIO.dumps.load_map_from_file(outfile)
    kvs = [(k, v) for k, v in phrase_freq.items()]
    phrase_freq_sorted = sorted(kvs, cmp=compare_kv, reverse=True)
    fileIO.dumps.dump_tuple_list_to_file(filename="./phrase_freq_sorted.text", tuple_list=phrase_freq_sorted)
