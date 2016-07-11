#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: extract_nn.py
@time: 3/24/16 2:31 PM
"""

import nltk
from nltk.corpus import stopwords


def write_key2list(key2list, filename="patent2keywords.text"):
    fd = open(filename, "w")

    for key, list in key2list.items():
        line = key + ","
        for v in list:
            line += str(v) + ","

        line += "\n"

        fd.write(line)

    fd.close()


def load_key2list(filename="patent2keywords.text"):
    fd = open(filename)

    lines = fd.readlines()
    key2list = {}
    for line in lines:
        tokens = line.strip('\n').split(',')
        key2list[tokens[0]] = []
        for word in tokens[1:]:
            key2list[tokens[0]].append(word)

    return key2list





def exact_keywords(sentence):

    tokens = nltk.word_tokenize(sentence)

    word_tags = nltk.pos_tag(tokens)
    print word_tags

    keywords = []

    en_stopwords = stopwords.words('english')
    NNType = ['NNS', 'NN', 'NNP', 'NNPS']
    i = 0
    word_count = len(word_tags)
    while i < word_count:
        if word_tags[i][0].lower() in en_stopwords:
            i += 1
            continue

        if word_tags[i][1] in NNType:
            try:
                if (word_tags[i+1][1] in NNType) and (word_tags[i+1][0].lower() not in en_stopwords):
                    keyword = word_tags[i][0] + " " + word_tags[i+1][0]
                    i += 2
                    keywords.append(keyword)
                else:
                    keyword = word_tags[i][0]
                    keywords.append(keyword)
                    i += 1
            except:
                keyword = word_tags[i][0]
                keywords.append(keyword)
                i += 1

        elif word_tags[i][1] in ['JJ']:
            if i + 1 < word_count:
                if (word_tags[i+1][1] in NNType) and (word_tags[i+1][1] not in en_stopwords):
                    keyword = word_tags[i][0] + " " + word_tags[i+1][0]
                    i += 2
                    keywords.append(keyword)
                else:
                    i += 1
            else:
                i += 1
        else:
            i += 1

        print i

    return keywords


if __name__ == '__main__':

    # title = "data center cooling system"
    # title = "tom is a cool boy"
    # title = "Wireless communication with a dock"
    # title = "Cryptographic methods, host system, trusted platform module, and computer arrangement"
    # title = "METHOD AND SYSTEM FOR MEASURED VALUE SIMULATION"
    # print exact_keywords(title)

    fd = open("../title", "r")
    lines = fd.readlines()

    patent2keywords = {}
    i = 0
    while i < len(lines)/2:

        patent = lines[2*i].strip('\n')
        sentence = lines[2*i+1].strip('\n')
        print sentence
        i += 1

        keywords = exact_keywords(sentence)
        if not keywords:
            continue

        patent2keywords[patent] = keywords

        print i


    print "extact keywords over"

    print patent2keywords

    write_key2list(patent2keywords)
    print load_key2list()








