#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: scan.py
@time: 6/14/16 2:22 PM
"""


from __init__ import *
from extract_field import extract_fields_from_item_list


class Scanner(object):
    def __init__(self, table_name, fields, service=default_service, region=default_region):
        self.client = boto3.client(service, region)
        self.table_name = table_name
        self.fields = fields
        self.last_key = None
        self.response = None
        # field_list = fields.split(',')
        # type_list = types.split(',')
        # self.field_type = {}
        # for i in range(len(field_list)):
        #     self.field_type[field_list[i]] = type_list[i]

    def scan_once(self, limit=3000):
        if self.last_key:
            self.response = self.client.scan(TableName=self.table_name,
                                             ProjectionExpression=self.fields,
                                             ExclusiveStartKey=self.last_key,
                                             Limit=limit)
        else:
            self.response = self.client.scan(TableName=self.table_name,
                                             ProjectionExpression=self.fields,
                                             Limit=limit)

        items = None
        try:
            items = self.response[u'Items']
            self.last_key = self.response[last_key_field]

        except:
            self.last_key = None

        return self.last_key, items


if __name__ == '__main__':
    scaner = Scanner(table_name='patent_title', fields='title,patent_id,lang')
    last_key, items = scaner.scan_once()

    field_values = extract_fields_from_item_list(items, {'title': 'B', "patent_id": "S", "lang": "S"})

    i = 0
    for title in field_values['title']:
        print title, field_values['patent_id'][i], field_values['lang'][i]
        i += 1

