#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: text_process.py
@time: 6/16/16 5:38 PM
"""


import nltk
from fileIO import load, dumps
import codecs
import re

def split_en_text_into_words_set(text, stopwords, method):

    word_set = set()
    try:
        mode = r'[a-zA-Z-]+$'
        pattern = re.compile(mode)
        sentence_list = nltk.sent_tokenize(text)
        for sentence in sentence_list:
            words = nltk.word_tokenize(sentence.lower())

            for w in words:

                if not pattern.match(w):
                    continue

                if len(w) < 4:
                    continue

                w = method(w)

                if w in stopwords:
                    continue

                word_set.add(w)
    except:
        pass

    return word_set


def get_words_frequency(filename, method):
    word_frequency = {}
    all_words = set()
    i = 0
    with codecs.open(filename=filename, mode='r', encoding='utf-8') as fd:
        while True:

            line = fd.readline().strip('\n')
            if not line:
                break

            text = u"".join(line.split(":")[1:])
            word_set = split_en_text_into_words_set(text, [], method)

            for w in word_set:
                # print w
                if w in all_words:
                    word_frequency[w] += 1
                else:
                    all_words.add(w)
                    word_frequency[w] = 1

            i += 1
            if i % 1000 == 0:
                print i/1000

    return word_frequency


def word_word_frequency(filename, word_set, method):
    word_word_freq = {}
    word_word_set = set()
    with codecs.open(filename=filename, mode='r', encoding='utf-8') as fd:
        while True:

            line = fd.readline().strip('\n')
            if not line:
                break

            text = u"".join(line.split(":")[1:])
            text_word_set = split_en_text_into_words_set(text, [], method)
            text_word_set = sorted(text_word_set)
            word_count = len(text_word_set)
            print word_count
            if word_count < 2:
                continue

            for i in range(word_count - 1):
                w1 = text_word_set[i]
                if w1 not in word_set:
                    continue

                j = i + 1
                while j < word_count:
                    w2 = text_word_set[j]
                    j += 1
                    if w2 not in word_set:
                        continue

                    key = w1 + "," + w2

                    if key in word_word_set:
                        word_word_freq[key] += 1
                    else:
                        word_word_set.add(key)
                        word_word_freq[key] = 1

    return word_word_freq


if __name__ == '__main__':

    # text = "A coupling arrangement (63;107;229) for use in a fluid pressure device including a gerotor gear set (15;83;205). The gerotor gear set includes an orbiting and rotating star (21;95;209). In a motor embodiment (FIGS. 1-4 and FIG. 6), the coupling (63;229) transmits the orbital and rotational movement of the star (21;209) to an output shaft (29;203). In a steering unit embodiment (FIG. 5) the orbital and rotational movement of the star (95) is transmitted as rotational follow-up movement to a sleeve valve (101). In either case, the invention eliminates the need for the conventional solid dogbone arrangement, thus making the device much less expensive and more compact, and giving the designer greater flexibility with regard to various options, such as the provision of thru-shaft capability for a motor."
    # stopwords = None
    # print split_en_text_into_words_set(text, stopwords=[])
    #

    # lemmatize = nltk.stem.WordNetLemmatizer().lemmatize



    stem = nltk.PorterStemmer().stem_word
    # word_frequency = get_words_frequency(filename="./data/abstract.text", method=stem)
    #
    # dumps.dump_map_to_file(word_frequency, "./result/stem_freq.text", mode='w')

    word_frequency = dumps.load_map_from_file("./result/stem_freq.text")

    high_freq_word_set = set()
    for w, freq in word_frequency.items():
        if int(freq) > 200:
            high_freq_word_set.add(w)

    print len(high_freq_word_set)

    # high_freq_word_set = sorted(high_freq_word_set)

    wwf = word_word_frequency("./data/abstract.text", high_freq_word_set, stem)

    dumps.dump_map_to_file(filename="./result/stem_stem_freq.text", dic=wwf)


