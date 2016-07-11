#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: UpdateToDynamodb.py
@time: 5/17/16 1:00 PM
"""


import boto3
import commands
import time
import codecs
import json
import multiprocessing
import traceback
import random


PROCESS_NUM = 2

#
# # get processed filename from logs
# def get_proccesd_file_list(log_name_collection):
#
#     cmd = ''' grep -r Processing %s |awk -F'/'  '{print $5}'| awk -F' ' '{print $1}' ''' %log_name_collection
#     status, output = commands.getstatusoutput(cmd)
#     processed_file_set = set(output.split())
#
#     return list(processed_file_set)
#
#
# # random choose an unprocessed file
# def choice_a_unprocessed_file(processed_file_list, unprocessed_file_list):
#
#     filename = None
#     while True:
#
#         if not unprocessed_file_list:
#             return None
#
#         filename = random.choice(unprocessed_file_list)
#
#         # num = int(filename.split('.')[0][1:])
#         #
#         # num_even_or_not = (num%2 == 0)
#         #
#         # if num_even_or_not == even_flag:  # even number
#         if filename in processed_file_list:
#             unprocessed_file_list.remove(filename)
#
#             # print "processed file", filename
#             continue
#
#         else:
#             processed_file_list.append(filename)
#             unprocessed_file_list.remove(filename)
#             # print "unprocessed file", filename
#             break
#         #
#         # else:
#         #     unprocessed_file_list.remove(filename)
#         #     print "filtered file", filename
#         #
#         #     continue
#
#     return filename


def load_label(filename, log_fd):
    with codecs.open(filename, "r", "utf-8") as fd:

        pre_pid = ""
        cur_pid = ""

        i = 0

        lines = fd.readlines()
        pid_labels = []

        for line in lines:
            try:

                item = json.loads(line.strip("\n"), encoding='utf-8')

                cur_pid = item['patent_id']

                if cur_pid == pre_pid:
                    continue
                else:
                    pre_pid = cur_pid

                pid_labels.append(item)

            except:

                log_fd.write("[ERRO]: load label fails, line: " + line)

        return pid_labels


def batch_write_to_dynamodb(table_name, pid_labels, batch_count, fd):

            n = 0
            start = time.time()
            item_num = 0
            request_items = {table_name: []}
            client = boto3.client('dynamodb')

            for pid_label in pid_labels:

                try:
                    item = {'PutRequest': {'Item': {}}}

                    for k, v in pid_label.items():
                        item['PutRequest']['Item'][k] = {'S': v}

                    gmt_msecond = int(time.time()*1000)
                    gmt_msecond_str = str(gmt_msecond)
                    item['PutRequest']['Item']['updated_ts'] = {'S': gmt_msecond_str}
                    item['PutRequest']['Item']['created_ts'] = {'S': gmt_msecond_str}

                    item['PutRequest']['Item']['version'] = {'N': '1'}

                    request_items[table_name].append(item)

                    n += 1

                    if n != batch_count:
                        pass
                        # print request_items[table_name]
                    else:

                        while True:

                            throutput = 500

                            time_splice = 1.0/(float(throutput)/batch_count/PROCESS_NUM)

                            begin = time.time()

                            response = client.batch_write_item(RequestItems=request_items)

                            time_elapsed = time.time() - begin
                            # print "update", time_elapsed
                            if time_splice > time_elapsed:
                                time.sleep(time_splice - time_elapsed)
                                fd.write("net io time less than time splice: " + str(time_elapsed) + "\n");
                            else:
                                fd.write("net io time more than time splice: " + str(time_elapsed) + "\n");
                                pass

                            if table_name in response['UnprocessedItems'].keys():

                                fd.write(response + "\n");
                                print len(response['UnprocessedItems'][table_name])
                                unprocessed_item = response['UnprocessedItems'][table_name]
                                request_items[table_name] = unprocessed_item

                                n = len(request_items[table_name])

                                if n < batch_count:
                                    break
                                else:
                                    time.sleep(1)

                            else:  # norequest_items unprocessed items

                                request_items[table_name] = []
                                n = 0
                                break

                except:
                    # print "[INFO]　unexpected error"
                    fd.write(u"[INFO] unexpected error\n")
                    fd.write(str(request_items[table_name]) + "\n")
                    print request_items[table_name]
                    request_items[table_name] = []
                    n = 0

                item_num += 1
                if item_num % 1000 == 0:
                    time_str = str(time.time() - start)
                    fd.write(time_str + "\n")
                    start = time.time()


def process_fun(tablename, filename, batch_count):
    start = time.time()

    f = filename.split("/")[-1]
    log_name = "./single_log/" + f

    log_fd = codecs.open(log_name, "w", "utf-8")

    try:
        pid_labels = load_label(filename, log_fd)
        batch_write_to_dynamodb(tablename, pid_labels, batch_count, log_fd)
    except:

        log_fd.write(traceback.format_exc() + "\n")

    timeElasped = time.time() - start

    info = "[Processing] " + filename + " timeElapsed " + str(timeElasped) + "\n"

    log_fd.write(info)
    log_fd.close()

if __name__ == '__main__':
    result_dir = "./label_json_dir"

    status, output = commands.getstatusoutput("ls " + result_dir)
    file_list = output.split()
    print file_list

    batch_count = 25

    tablename = "landscape_feature"
    pool = multiprocessing.Pool(processes=PROCESS_NUM)

    for f in file_list:

        log_name = "./single_log/" + f
        f = result_dir + "/" + f

        print f

        pool.apply_async(process_fun, (tablename, f, batch_count))

        start = time.time()

    pool.close()
    pool.join()

