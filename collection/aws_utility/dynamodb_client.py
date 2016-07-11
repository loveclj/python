#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: dynamodb_client.py.py
@time: 3/23/16 11:19 AM
"""
import boto3


def connect_dynamodb():
    client = boto3.client("dynamodb")
    return client


class DynamodbClient(object):

    def __init__(self, table_name, primary_key_name, primary_key_type,
                 sort_key_name=None, sort_key_type=None, nbatch=50):

        self.table_name = table_name
        self.client = connect_dynamodb()
        self.primary_key = primary_key_name
        self.primary_key_type = primary_key_type
        self.sort_key_type = sort_key_type
        self.sort_key_name = sort_key_name
        self.nBatch = nbatch

    def batch_get_item(self, key_list, sort_key, attribute_str):
        attribute_list = attribute_str.strip(' ').split(",")

        total_item = len(key_list)
        index_list = []

        while True:
            index_list.append(total_item)
            total_item -= self.nBatch
            if total_item <= 0:
                index_list.append(0)
                break

        index_list.sort()
        print index_list[1:]

        items = []
        batch_get_count = len(index_list) - 1
        i = 0
        while i < batch_get_count:

            begin = index_list[i]
            end = index_list[i+1]

            query = {self.table_name: {'Keys': []}}
            query[self.table_name]['AttributesToGet'] = attribute_list
            while begin < end:
                key_conditions = {self.primary_key: {self.primary_key_type: patent_list[begin]}}
                if self.sort_key_name is not None:
                    key_conditions[self.sort_key_name] = {self.sort_key_type: sort_key}

                query[self.table_name]['Keys'].append(key_conditions)

                begin += 1

            i += 1
            print query
            response = self.client.batch_get_item(RequestItems=query)
            print response
            items.extend(response['Responses'][self.table_name])

        print items






if __name__ == '__main__':
    test = DynamodbClient(table_name="patent_title", primary_key_name="patent_id",
                          primary_key_type="S", sort_key_type="S", sort_key_name="lang", nbatch=2)
    patent_list = ["1986975f-d2e1-44de-b32f-29c8211586fe", "450573c3-8eac-4827-bd09-bb72459266f4", "06cc7708-ed29-4ed0-986d-aec0b0493856"]
    test.batch_get_item(patent_list, "EN", "update_ts,patent_id")