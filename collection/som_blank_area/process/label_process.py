#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: label_process.py
@time: 4/14/16 4:53 PM
"""


import aws_utility.dynamodb as dynamodb


def dumps_map(m, filename):
    with open(filename, "w") as fd:
        for key, v in m.items():
            string = str(key) + '\n'
            fd.write(string)

            string = v + '\n'
            string = string.replace('.', '')
            fd.write(string)

def save_dynamo_label(jobid, filename):

    table = dynamodb.Table2(table_name="landscape_label_test", partition_key='job_id')
    try:
        grid2label = table.get_item(jobid)[u'Item'][u'text_label']

        with open(filename, "w") as  fd:
            for k, v in grid2label.items():
                fd.write(k + '\n')
                fd.write(v + '\n')
    except:
        pass

def load_label(filename, grid2label):
    with open(filename, "r") as fd:
        lines = fd.readlines()
        count = len(lines)/2
        for i in range(count):
            grid = lines[2*i].strip('\n')
            label = lines[2*i+1].strip('\n')
            grid2label[grid] = label





if __name__ == '__main__':
    # save_dynamo_label("test1000", "original_label.text")

    grid2label = {}
    load_label("original_label.text", grid2label)
    load_label("../blank_label.text", grid2label)
    print grid2label

    table = dynamodb.Table2("landscape_label_test", "job_id")
    table.update_item(partition_key="test1000", attribute="text_label", value=grid2label)
