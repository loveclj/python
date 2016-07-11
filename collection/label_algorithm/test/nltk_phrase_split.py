#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: nltk_phrase_split.py
@time: 4/1/16 1:31 PM
"""


import nltk
import time
# import label_algorithm.text_process as text_process


def split_as_phrase(sentence, parser, stopwords):

    sentence = sentence.replace('”', '')
    words = nltk.word_tokenize(sentence.lower())
    sentence_tagged = nltk.pos_tag(words)

    sentence_split = parser.parse(sentence_tagged)

    phrase_str = ""

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
                print node[0]

    print sentence.lower()
    print phrases
    return phrases


def split_cn_as_phrase(sentence, parser, stopwords):

    sentence = sentence.decode('utf-8')

    words = nltk.word_tokenize(sentence)


    sentence_tagged = nltk.pos_tag(words)

    sentence_split = parser.parse(sentence_tagged)

    sentence_split.draw()


def sentence_parse(grammar):
    return nltk.RegexpParser(grammar)


def extract_keywords(sentence):
    title_grammar = "NP: {<DT>?<JJ>?<NNS>?<NN>}"
    title_grammar = "NP: {<NNS|NN|NNP|NNPS|JJ><NN|NNS>}"

    parser = sentence_parse(title_grammar)

    fd = open('../title', 'r')
    lines = fd.readlines()
    fd.close()
    nSentence = len(lines)/2
    i = 0

    start = time.time()

    wfd = open("phrase.text", "w")

    stopwords = text_process.load_list("../stopword_process/stopwords_update.text")

    keywords = split_as_phrase(sentence, parser, stopwords)
    return keywords



if __name__ == '__main__':
    title_grammar = "NP: {<DT>?<JJ>?<NNS>?<NN>}"
    title_grammar = "NP: {<NNS|NN|NNP|NNPS|JJ><NN|NNS>}"

    parser = sentence_parse(title_grammar)

    # fd = open('../title', 'r')
    # lines = fd.readlines()
    # fd.close()
    # nSentence = len(lines)/2
    # i = 0
    #
    # start = time.time()
    #
    # wfd = open("phrase.text", "w")
    #
    # stopwords = text_process.load_list("../stopword_process/stopwords_update.text")

    #
    # while i < nSentence:
    #     line = lines[2*i+1].strip('\n')
    #     i += 1
    #     phrase_combination = split_as_phrase(line, parser, stopwords)
    #
    #     wfd.write(line + "\n")
    #     wfd.write(phrase_combination)
    #     wfd.write('\n')
    #     wfd.write("--------------------------------" +'\n')
    #
    #
    #
    #
    # wfd.close()


    # sentence = "Efficient movement of storage media in a storage media library"
    # sentence = "我是中国人"
    #
    #
    # rlt = split_cn_as_phrase(sentence, parser, [])

    start = time.time()
    sentence1 = "data center cooling system"
    sentence2 = "meeting center cooling car"
    sentence3 = "boil center cooling cow"


    split_as_phrase(sentence1, parser, [])
    split_as_phrase(sentence2, parser, [])
    split_as_phrase(sentence3, parser, [])
    print time.time() - start





    # print "time elapsed ", time.time() - start
    # rlt.draw()