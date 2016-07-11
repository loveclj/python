#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: test.py
@time: 4/29/16 5:31 PM
"""

import codecs
import time


def get_word_freq(filename):


        keyword_freq = {}
        words_set = set()

        fd = codecs.open(filename, "r", "utf-8")

        k = 0

        # for line in fd.readline():
        while True:

            line = fd.readline()
            line = line.strip('\n')

            if not line:
                break

            try:
                keywords = line.split(":")[1].split(',')
                for w in keywords:
                    if w in words_set:
                        keyword_freq[w] += 1

                    else:
                        keyword_freq[w] = 1
                        words_set.add(w)
            except:
                print line


            k += 1

            if k%10000 == 0:
                print k/10000

        fd.close()

        fd = codecs.open("cn_word_freq.text", "w", "utf-8")
        for k, v in keyword_freq.items():
            line = k + u":" + str(v) + u"\n"
            fd.write(line)

        fd.close()


def key_word_freq(filename, n, outfile_name):
    fd = codecs.open(filename, "r", "utf-8")
    lines = fd.readlines()
    k = 0

    ofd = codecs.open(outfile_name, "w", "utf-8")

    freq_set = set()
    freq_count = {}
    for line in lines:
        line = line.strip('\n').split(':')

        freq = eval(line[1])

        if freq in freq_set:
            freq_count[freq] += 1
        else:
            freq_set.add(freq)
            freq_count[freq] = 1

        if freq > n:
            print line
            ofd.write(line[0] + ":" + line[1] + "\n")

        k += 1

        if k %10000 == 1:
            print k/10000

    ofd.close()
    fd.close()

    return freq_count

if __name__ == '__main__':

    # EN
    # n = 10000
    # filename = "en_word_freq.text"
    # freq_count = key_word_freq(filename, n, "high_frequency_words.text")
    #
    # freq_count_file = "freq_count.text"
    # fd = open(freq_count_file, "w")
    #
    # for k, v in freq_count.items():
    #     line = str(k) + " " + str(v) + "\n"
    #
    #     fd.write(line)
    #
    # fd.close()

    # get_word_freq("/home/lizhifeng/sourceCode/pycharm/patent_title_preprocess/cn_pid2keywords.text")
    key_word_freq("cn_word_freq.text", 1000, "cn_high_frequency_words.text")




    # for k, v in freq_count.items():
    #     print k, v