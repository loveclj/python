#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: extract_cn_label.py.py
@time: 4/28/16 11:35 AM
"""
import jieba.posseg as posseg
import jieba
import boto3
import codecs

import time

import process

def load_list(filename="stopwords"):
    fd = codecs.open(filename, "r", 'utf-8')
    lines = fd.readlines()
    words_list = []

    for line in lines:
        words_list.append(line.strip('\n'))

    fd.close()
    words_set = set(words_list)
    return words_set


class FilterScanner(object):
    def __init__(self, tablename, attribute_get, filter):
        self.tablename = tablename
        self.table = boto3.resource('dynamodb').Table(tablename)
        self.filter = filter

        self.attribute_get = attribute_get

    def scan(self, lastkey=None):
        if lastkey:
            response = self.table.scan(ExclusiveStartKey=lastkey, AttributesToGet=self.attribute_get, ScanFilter=self.filter)
        else:
            response = self.table.scan(AttributesToGet=self.attribute_get, ScanFilter=self.filter)

        if response[u'Count'] > 0:
            if u'LastEvaluatedKey' in response.keys():
                return response[u'Items'], response[u'LastEvaluatedKey']
            else:
                return response[u'Items'], None
        else:
            return None, lastkey


def get_cn_title_from_dynamodb(filename):
    fields = ['patent_id', 'title']
    filter = {'lang':{'AttributeValueList': ['CN'], 'ComparisonOperator': 'EQ' }}
    title_scanner = FilterScanner(tablename='patent_title', attribute_get=fields, filter=filter)

    fd = codecs.open(filename, 'w', 'utf-8')
    lastkey = None

    while True:
        start = time.time()
        items, lastkey = title_scanner.scan(lastkey)
        print time.time() - start
        print len(items)

        start = time.time()
        for item in items:
            title = unicode(process.binary2string(item['title']), 'utf-8')
            pid = item['patent_id']
            line = pid + u':' + title + u'\n'
            # print line,
            fd.write(line)
        print time.time() - start

        time.sleep(0.5)

        if not lastkey:
            break

    fd.close()


def extract_key_cn_words(filename, out_filename):
    fd = codecs.open(filename, "r", "utf-8")
    out_fd = codecs.open(out_filename, "w", "utf-8")

    stopwords = load_list("cnStopwords")
    print stopwords


    i = 0
    while True:
        line = fd.readline()

        print line

        if not line:
            break

        kv = line.strip('\n').split(':')
        pid = kv[0]
        title = kv[1]

        # title = u"数据中心制冷系统"
        # title = "一种治疗女性痛经的中药"
        words = jieba.cut(title, cut_all=False)


        seg_list = []
        for word in words:
            if len(word) < 2 or word in stopwords:
                # print word
                continue
            seg_list.append(word)


        i += 1

        # print i
        # print title
        # print pid, ",".join(seg_list)

        out_line = pid + u":" + u",".join(seg_list) + u'\n'
        out_fd.write(out_line)
        # print out_line

    out_fd.close()
        # words = posseg.cut(title)
        # keywords = u""
        # for word, flag in words:
        #     keywords += word + u" " + flag + u","
        #
        # i += 1
        # print i
        # print title
        # print pid, keywords


if __name__ == '__main__':
    get_cn_title_from_dynamodb("title_cn.text")
    extract_key_cn_words("title_cn.text", "cn_pid2keywords.text")
