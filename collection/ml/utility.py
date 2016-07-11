__author__ = 'lizhifeng'

import StringIO
import gzip
import re
import enchant
import nltk.corpus


def binary2string(encode):
    obj = StringIO.StringIO(encode)
    gzip_obj = gzip.GzipFile(fileobj=obj)
    decode = gzip_obj.read()
    gzip_obj.close()
    return decode


def clean_content(content):
    result = re.sub(r'\W', " ", content)
    return result


def split_sentence_to_words(sentence):

    _checker = enchant.Dict("en_US")
    _stop_words = nltk.corpus.stopwords.words("english")

    _clean_sentence = clean_content(sentence.lower())
    _words_list = _clean_sentence.split()
    _words_list = [w for w in _words_list if len(w) > 2 and _checker.check(w) and w not in _stop_words]

    return _words_list

