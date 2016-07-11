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
            return self.table.scan(ExclusiveStartKey=lastkey, AttributesToGet=self.attribute_get)
        else:
            return self.table.scan()


if __name__ == '__main__':
    tablename = "patent_title"
    attribute_get = ['lang', 'patent_id', 'title']
    scanner = Scanner(tablename, attribute_get)

    start = time.time()
    response = scanner.scan()
    lastkey = response['LastEvaluatedKey']
    print time.time() - start
    print lastkey
    response = scanner.scan(lastkey)
    print len(response[u'Items'])
    print(response[u'Items'][7000])
    lastkey = response['LastEvaluatedKey']
    print lastkey

