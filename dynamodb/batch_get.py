#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: batch_get.py
@time: 6/15/16 12:02 PM
"""
from __init__ import *


class BatchGet(object):
    def __init__(self, table_name, fields, max_batch_count=100, region=default_region):
        self.table_name = table_name
        self.fields = fields
        self.region = region
        self.max_batch_count = max_batch_count;
        self.client = boto3.client('dynamodb', self.region)

    def batch_get_once(self, key_list):
        response = ""
        if len(key_list) > self.max_batch_count:
            print "[Error] query too many items on time"
        else:
            request_items = {self.table_name: {'Keys': key_list, 'AttributesToGet': self.fields}}
            response = self.client.batch_get_item(RequestItems=request_items)

        return response


if __name__ == '__main__':
    pass