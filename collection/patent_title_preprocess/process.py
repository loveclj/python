#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: process.py
@time: 4/26/16 4:17 PM
"""
import StringIO
import gzip
import nltk
import time


def load_list(filename="stopwords"):
    fd = open(filename, "r")
    lines = fd.readlines()
    words_list = []

    for line in lines:
        words_list.append(line.strip('\n'))

    words_set = set(words_list)
    return words_set


def binary2string(encode):
    obj = StringIO.StringIO(encode)
    gzip_obj = gzip.GzipFile(fileobj=obj)
    decode = gzip_obj.read()
    gzip_obj.close()
    return decode


def split_as_phrase(sentence, parser, stopwords):

    sentence = sentence.replace('”', '')
    words = nltk.word_tokenize(sentence.lower())
    sentence_tagged = nltk.pos_tag(words)
    # print sentence_tagged

    sentence_split = parser.parse(sentence_tagged)

    lemmatize = nltk.stem.WordNetLemmatizer().lemmatize
    # print sentence_tagged658
    phrases = ""
    for node in sentence_split:

        if type(node) is nltk.Tree:
            words = []
            for sub_node in node:
                if sub_node[0] not in stopwords:
                    words.append(sub_node[0])

            if words:
                words[-1] = lemmatize(words[-1])
                phrases += " ".join(words) + ","
        else:
            if node[0] not in stopwords and node[0] != ',':
                phrases += lemmatize(node[0]) + ","
            else:
                # print node[0]
                pass

    # print sentence.lower()
    # print phrases
    return phrases


def sentence_parse(grammar):
    return nltk.RegexpParser(grammar)


if __name__ == '__main__':
    grammar = "NP: {<DT>?<JJ>?<NNS>?<NN>}"
    grammar = "NP: {<NNS|NN|NNP|NNPS|JJ><NN|NNS>}"

    parser = sentence_parse(grammar)

    stopwords = load_list("stopwords.text")

    start = time.time()


    sentence = "Efficient movement of storage media in a storage media library"
    # sentence = "我是中国人"

    rlt = split_as_phrase(sentence, parser, stopwords)

    print time.time() - start





    # print "time elapsed ", time.time() - start
    # rlt.draw()



