__author__ = 'lizhifeng'

#coding=utf-8

import re
import random
import pymongo
import gensim
import numpy as np
import matplotlib.pyplot as plt
import snowballstemmer
import string

from sklearn.metrics.pairwise import  cosine_similarity
from sklearn.cluster import  AgglomerativeClustering
from nltk.corpus import  stopwords
import nltk

from aws4_signature import GetDynamodbClient
from utility import binary2string
from dynamodb_api import *
from utility import *

porterStemWord = snowballstemmer.PorterStemmer().stemWord


if __name__ == "__main__":

    region = "cn-north-1"
    endpoint = 'http://dynamodb.cn-north-1.amazonaws.com.cn'
    key_path = "/home/lizhifeng/.ssh/.aws_key"

    client = GetDynamodbClient(key_path, region, endpoint)

    patent_list = get_patent_ids_from_file("pid_100")

    stopwords_en = stopwords.words('english')

    patent_title = batch_get(client, patent_list, "patent_title", "lang", "patent_id", "title")
    patent_abstract = batch_get(client, patent_list, "patent_abstract", "lang", "patent_id", "abstract")

    key_word = {}
    for key in patent_title.keys():
        title = patent_title[key]
        words = split_sentence_to_words(title)
        key_word[key] = words

    for key in patent_abstract.keys():
        abstract = patent_abstract[key]
        words = split_sentence_to_words(abstract)
        if key not in key_word.keys():
            key_word[key].extend(words)
        else:
            key_word[key] = words

    for key, val in key_word.items():
        print key
        print val















