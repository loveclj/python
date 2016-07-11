#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: test.py.py
@time: 4/27/16 10:53 AM
"""
import codecs
import multiprocessing
import jieba
import re


def fun(x):
    while True:
        print x
        x += 1

def test_fun():
    x = 1
    p =multiprocessing.Process(target=fun, args=(x,))
    p.start()
    while True:
        print x

    p.join()

def split_cn_sentence_as_phrase(sentence, stopwords, mode):

        result = ""

        try:
            words = jieba.cut(sentence, cut_all=False)
            seg_list = []
            for word in words:

                if len(word) < 2 or len(word) > 6 or word in stopwords or mode.match(word):
                    continue

                seg_list.append(word)

            result = u";".join(seg_list)

        except:
            print "[Error]: split cn sentence fail, sentence:", sentence

        return result




if __name__ == '__main__':

    # fd = codecs.open("t", "a", "utf-8")
    # fd.write(u"women’s underwear,\n")
    #    throutput = 250
    #    process_num = 4
    #    batch_count = 25
    #    time_splice = 1.0/(float(throutput)/batch_count/process_num)
    #    print time_splice

    s = u"数据中心制冷系统，love,ex124ro, 332, b"
    mode = re.compile(r'[0-9]+$')
    print split_cn_sentence_as_phrase(s, [], mode)

