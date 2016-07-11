#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: dynamodb.py.py
@time: 3/21/16 1:43 PM
"""

import boto3


class Table(object):

    def __init__(self, table_name, partition_key, sort_key):
        self.table_name = table_name
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table(table_name)
        self.partition_key = partition_key
        self.sort_key = sort_key

    def get_item(self, partition_key, sort_key):
        key_expression = {self.partition_key: partition_key, self.sort_key: sort_key}
        return self.table.get_item(Key=key_expression)


class Table2(object):

    def __init__(self, table_name, partition_key):
        self.table_name = table_name
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table(table_name)
        self.partition_key = partition_key

    def get_item(self, partition_key):
        key_expression = {self.partition_key: partition_key}
        return self.table.get_item(Key=key_expression)

    def update_item(self, partition_key, attribute, value):
        key = {self.partition_key: partition_key}
        update_expression = "SET " + attribute + " = :val1"
        print key
        print update_expression
        attribute_value = {":val1": value }
        print attribute_value
        return self.table.update_item(Key=key, UpdateExpression=update_expression, ExpressionAttributeValues=attribute_value)


if __name__ == '__main__':
    pass