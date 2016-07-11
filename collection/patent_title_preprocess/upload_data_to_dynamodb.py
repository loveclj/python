#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: upload_data_to_dynamodb.py
@time: 5/3/16 4:10 PM
"""

import boto3
import commands
import time


def load_pid_keywords(filename):

    pid_keyword = {}

    with open(filename) as fd:
        lines = fd.readlines()
        for line in lines:
            try:
                line = line.strip('\n').split(':')
                pid = line[0]

                legal_words = []
                for w in line[1:]:
                    if len(w) < 3:
                        continue
                    else:
                        legal_words.append(w)

                keywords = ""
                if legal_words:
                    keywords = ",".join(legal_words)
                else:
                    continue

                pid_keyword[pid] = keywords
            except:
                print line

    return pid_keyword


# def batch_write_to_dynamodb(table_name, kv):
#     table = boto3.resource('dynamodb').Table(table_name)
#
#     with table.batch_writer() as batch:
#
#             start = time.time()
#             item_num = 0
#
#             for k, v in kv.items():
#                 try:
#                     batch.put_item(Item={'patent_id': k, "lang_en": v})
#                 except:
#                     print "[Error] Patent_id:", k, v
#
#                 item_num += 1
#
#                 if item_num % 10 == 0:
#                     print time.time() - start
#                     start = time.time()


def batch_write_to_dynamodb(table_name, kv):
            client = boto3.client('dynamodb')

            batch_count = 4
            n = 0
            start = time.time()
            item_num = 0
            request_items = {table_name: []}

            for k, v in kv.items():
                try:
                    item = {'PutRequest': {'Item': {'patent_id': {'S': k}, 'lang_en': {'S': v}}}}
                    # item = {'DeleteRequest': {'Key': {'patent_id': {'S': k}}}}
                    request_items[table_name].append(item)

                    n += 1
                    if n != batch_count:
                        pass
                        # print request_items[table_name]
                    else:

                        time.sleep(0.5)
                        print request_items
                        response = client.batch_write_item(RequestItems=request_items)
                        print response

                        if table_name in response['UnprocessedItems'].keys():
                            print len(response['UnprocessedItems'][u'landscape_preprocess_test'])
                            unprocessed_item = response['UnprocessedItems'][table_name]
                            request_items[table_name] = unprocessed_item

                            time.sleep(1)

                            response = client.batch_write_item(RequestItems=request_items)

                            print "re-send", response

                        request_items[table_name] = []
                        n = 0

                except:
                    print "[Error] Patent_id:", k, v
                    n = 0

                item_num += 1

                if item_num %100 == 0:
                    print time.time() -start
                    start = time.time()


if __name__ == '__main__':
    result_dir = "./first_result_lang_en_env_cn/result"
    status, output = commands.getstatusoutput("ls " + result_dir)
    file_list = output.split()

    for f in file_list:
        f = result_dir + "/" + f
        start = time.time()

        pid_keywords = load_pid_keywords(f)

        print time.time() - start

        batch_write_to_dynamodb("landscape_preprocess_test", pid_keywords)

        print f, time.time() - start