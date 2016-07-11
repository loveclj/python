#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: update.py.py
@time: 2/29/16 11:58 AM
"""


import boto3

class UpdateObj(object):
    def __init__(self, tablename):
        self.table = boto3.resource('dynamodb').Table(tablename)

    def update(self, **arg):
        self.table.update_item(arg)

    def update_fun(self):
        return self.table.update_item


if __name__ == '__main__':
    table_name = "landscape_label"
    update_obj = UpdateObj(table_name)
    update = update_obj.update_fun()
    update(Key={'job_id':''
                         ''},
                            UpdateExpression='SET age = :val1', ExpressionAttributeValues={':val1':25})