#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: batch_get.py.py
@time: 4/28/16 10:08 AM
"""
import boto3


class BatchGet(object):
    def __init__(self, table_name, primary_key_name, range_key_name, attribute_to_get):
        self.table_name = table_name
        self.primary_key_name = primary_key_name
        self.range_key_name = range_key_name
        self.attribute_to_get = attribute_to_get
        self.client = boto3.client('dynamodb')

        self.batch_count = 100

        self.request_items = {}
        self.request_items[self.table_name] = {}
        self.request_items[self.table_name]['Keys'] = []
        self.request_items[self.table_name]['AttributesToGet'] = self.attribute_to_get

    def get_by_list(self, key_list):
        items = []
        item_count = len(key_list)/self.batch_count

        print item_count
        for i in range(item_count+1):
            print i

            self.request_items[self.table_name]['Keys'] = key_list[i*self.batch_count:(i+1)*self.batch_count:1]

            response = self.client.batch_get_item(RequestItems=self.request_items)
            items.extend(response[u'Responses']['patent_title'])

            if response['UnprocessedKeys']:
                while True:
                    self.request_items[self.table_name]['Keys'] = response['UnprocessedKeys']
                    response = self.client.batch_get_item(RequestItems=self.request_items)
                    items.extend(response[u'Responses']['patent_title'])

                    if not response['UnprocessedKeys']:
                        break


        return items


if __name__ == '__main__':
    pass