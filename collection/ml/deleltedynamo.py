#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: deleltedynamo.py.py
@time: 1/29/16 3:30 PM
"""

import boto3


class TableObj:
    def __init__(self, tablename, method):
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table(tablename)
        # self.response = self.table.scan()
        self.method = method
        self.key_schema = {}

    def operation(self):
        self.method(self.table)


def parse_key_schema(table):
    key_schema = {}
    for item in table.key_schema:
        if item['KeyType'] != u'RANGE':
            key_schema['key'] = item['AttributeName']
        else:
            key_schema['range'] = item['AttributeName']
    return key_schema


def clear_table(table):
    response = table.scan()

    key_schema = parse_key_schema(table)

    items = response[u'Items']
    print len(items)

    with table.batch_writer() as batch:
        for item in items:
            body = {}
            for k, v in key_schema.items():
                body[v] = item[v]
            # print(body)
            batch.delete_item(
                Key=body
            )

if __name__ == '__main__':
    tables = {}
    # tables["landscape_preprocess_test"] = "landscape_preprocess_test"
    # tables["in_facet"] = "landscape_in_facet_test"
    # tables["an_facet"] = "landscape_an_facet_test"
    # tables["ans_facet"] = "landscape_ans_facet_test"
    # tables["ipc_facet"] = "landscape_ipc_facet_test"
    # tables["label"] = "landscape_label_test"
    # tables["landscape"] = "landscape_test"
    # tables["match_result"] = "landscape_match_result_test"
    # tables["list_data"] = "landscape_patent_list_data_test"
    # tables["map_data"] = "landscape_patent_map_data_test"
    # tables["som_grid"] = "landscape_som_grid_test"
    tables["landscape_title"] = "landscape_title_test"
    tables["landscape_feature_sync"] = "landscape_feature_sync"

    for k, v in tables.items():
        print "clear", v
        obj = TableObj(v, clear_table)
        obj.operation()
