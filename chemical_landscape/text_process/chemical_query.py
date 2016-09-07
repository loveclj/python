#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: chemical_query.py
@time: 7/28/16 5:50 PM
"""

import boto3

import str_utilties



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
    for line in open(file_name):
        kv = line.strip('\n').strip('')
        if not kv:
            continue

        print kv
        cluster, inchi_value = kv.split(',')


        res = client.query(index_name=index_name, index=inchi_value)['Items']

        for rec in res:

            line = rec['cid']['N'] + "," + rec['inchi_key']['S'] + "," + cluster + '\n'
            fd.write(line)

    fd.close()


def get_cid_smiles_fingerprint_from_dynamodb_without_cluster(file_name, out_file_name, client, index_name):
    fd = open(out_file_name, 'w')
    for line in open(file_name):
        inchi_value = line.strip('\n').strip('')
        if not inchi_value:
            continue

        res = client.query(index_name=index_name, index=inchi_value)['Items']
        print res

        for rec in res:

            line = rec['cid']['N'] + "," + rec['inchi_key']['S'] + '\n'
            fd.write(line)

    fd.close()




if __name__ == '__main__':
    table = Table(table_name='chemical', partition_key='cid')

    get_cid_smiles_fingerprint_from_dynamodb_without_cluster(file_name="inchi_key_for_mds_64", out_file_name='test_data_simles_MDS_64.text', client=table, index_name='inchi_key')

    # with open('test_data_MDS_64_SMILES_fingerprint.text', "w") as out_fd, open('test_data_simles_MDS_64.text', 'r') as in_fd:
    #     N = 100
    #     i = 0
    #     while True:
    #         line = in_fd.readline().strip('\n')
    #         if not line:
    #             break
    #
    #         cid, inchi_key = line.split(',')
    #         # formula = table.get_item({'N': cid})['Item']["molecular_formula"]['S']
    #         formula = table.get_item({'N': cid})['Item']["smiles"]['L'][0]['M']['value']['S']
    #         fingerprint = table.get_item({'N': cid})['Item']["fingerprint"]['B']
    #         fingerprint = str_utilties.str2binary(fingerprint)
    #         print fingerprint
    #         name = 'unknow'
    #         try:
    #             name = table.get_item({'N': cid})['Item']["names"]['M']['EN']['L'][0]['S']
    #         except:
    #             pass
    #
    #         print name
    #         line = name + ',' + formula + ',' + fingerprint + '\n'
    #         out_fd.write(line)
    #
