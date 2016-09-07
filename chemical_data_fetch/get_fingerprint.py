#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: get_fingerprint.py
@time: 8/26/16 10:24 AM
"""

import boto3



def char2binary(c):
    b = bin(c)[2:]
    b = '0' * (8 - len(b)) + b
    return b


def str2binary(s, binary_begin=32, binary_end=-7):
    binary_list = map(char2binary, bytearray(s))
    binary = "".join(binary_list)[binary_begin: binary_end]
    return binary

class Table(object):

    def __init__(self, table_name, partition_key):
        self.table_name = table_name
        self.dynamodb = boto3.client('dynamodb')
        self.table_name = table_name
        self.partition_key = partition_key

    def get_item(self, partition_key):
        key_expression = {self.partition_key: partition_key}
        return self.dynamodb.get_item(TableName=self.table_name, Key=key_expression)

    def query(self, index_name, index):
        keyconditon = index_name + "= :val"
        index_name_index = index_name + "-index"
        return self.dynamodb.query(TableName=self.table_name, IndexName=index_name_index,
                                   KeyConditionExpression=keyconditon,
                                   ExpressionAttributeValues={':val': {'S': index}})


def get_cid_smiles_fingerprint_from_dynamodb(file_name, out_file_name, client, index_name):
    fd = open(out_file_name, 'w')
    fingerprint_set = set()
    for line in open(file_name):
        kv = line.strip('\n').strip('\r').strip('')
        if not kv:
            continue

        segs = kv.split(' ')
        # print segs
        # break
        name = segs[0]
        inchi_value = segs[-1]

        res = client.query(index_name=index_name, index=inchi_value)['Items']

        if not res:
            print name, "not found"
            continue

        cid = res[0]['cid']['N']
        # print cid

        formula = table.get_item({'N': cid})['Item']["smiles"]['L'][0]['M']['value']['S']

        fingerprint = table.get_item({'N': cid})['Item']["fingerprint"]['B']

        fingerprint = str2binary(fingerprint)

        if fingerprint in fingerprint_set:
            print "ignore", name
            continue
        else:
            fingerprint_set.add(fingerprint)

        line = name + ',' + formula + ',' + fingerprint + '\n'
        print line
        fd.write(line)

    fd.close()


if __name__ == '__main__':
    table = Table(table_name='chemical', partition_key='cid')

    get_cid_smiles_fingerprint_from_dynamodb(file_name="name_inchi_150k.text", out_file_name='name_formula_fingerprint_150k.text', client=table, index_name='inchi_key')
