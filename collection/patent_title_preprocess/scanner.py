#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: patent_scan.py.py
@time: 2/24/16 6:09 PM
"""
import boto3
import time


class Scanner(object):
    def __init__(self, tablename, attribute_get):
        self.tablename = tablename
        self.table = boto3.resource('dynamodb').Table(tablename)

        self.attribute_get = attribute_get

    def scan(self, lastkey=None):
        if lastkey:
            response = self.table.scan(ExclusiveStartKey=lastkey, AttributesToGet=self.attribute_get)
        else:
            response = self.table.scan(AttributesToGet=self.attribute_get)

        if response[u'Count'] > 0:
            if u'LastEvaluatedKey' in response.keys():
                return response[u'Items'], response[u'LastEvaluatedKey']
            else:
                return response[u'Items'], None
        else:
            return None, lastkey


if __name__ == '__main__':
    tablename = "patent_title"
    attribute_get = ['lang', 'patent_id', 'title']
    scanner = Scanner(tablename, attribute_get)

    start = time.time()
    items, lastkey = scanner.scan()

    print time.time() - start
    print lastkey
    response = scanner.scan(lastkey)


    items, lastkey = scanner.scan()
    print lastkey