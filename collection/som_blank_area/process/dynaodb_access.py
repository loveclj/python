#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: dynaodb_access.py
@time: 4/14/16 3:53 PM
"""


import aws_utility.dynamodb as dynamodb
import nltk
import time
import label_algorithm.text_process as text_process


def split_as_phrase(sentence, parser, stopwords):
    sentence = sentence.replace(u"”", '')
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
            if node[0] not in stopwords and len(node[0]) > 3:

                if node[1] not in ["NN", "NNS", "NNP", "NNPS", "JJ"]:
                    pass
                else:
                    phrases += lemmatize(node[0]) + ","

            else:
                # print node[0]
                pass
    print phrases
    return phrases




def sentence_parse(grammar):
    return nltk.RegexpParser(grammar)


def extract_keywords(sentence):

    title_grammar = "NP: {<NNS|NN|NNP|NNPS|JJ><NN|NNS>}"

    parser = sentence_parse(title_grammar)

    stopwords = text_process.load_list("../../label_algorithm/stopword_process/stopwords_update.text")

    keywords = split_as_phrase(sentence, parser, stopwords)
    return keywords

def get_label_by_ipc(ipcs):

    keywords_freq = {}
    table = dynamodb.Table2(table_name="patent_classification_ipc", partition_key='ipc')
    descr_list = []
    for ipc in ipcs:
        try:
            descr = table.get_item(ipc)[u'Item'][u'description_en']
            descr_list.append(descr)
        except:
            pass

    for descr in descr_list:
        keywords_str = extract_keywords(descr.replace(';', ','))

        list = keywords_str[:-2].split(',')

        for word in list:
            if not word:
                continue

            if word not in keywords_freq.keys():
                keywords_freq[word] = 1
            else:
                keywords_freq[word] += 1

    return keywords_freq


def get_label_from_dyanmodb(jobid, tablename):
        table = dynamodb.Table2(table_name=tablename, partition_key='job_id')
        print table.get_item(jobid)[u'Item'][u'text_label']



if __name__ == '__main__':
    # keywords = get_label_by_ipc(["A61", "A61K"])
    # print keywords

    get_label_from_dyanmodb('test1000', "landscape_label_test")


