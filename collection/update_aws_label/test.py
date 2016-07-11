#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: test.py.py
@time: 5/17/16 12:12 PM
"""
import json
import commands
import random
import codecs
import boto3

ss = {'landscape_preprocess_test': [{'PutRequest': {'Item': {'created_ts': {'S': '1463469216387'}, u'label_cn': {'S': u'\u8fd1\u573a;\u663e\u5fae\u955c;\u626b\u63cf;\u5149/\u539f\u5b50\u529b'}, u'patent_id': {'S': u'00000ba0-c256-4ed4-bed3-0e173382f1c5'}, 'version': {'N': '1'}, u'label_en': {'S': u'SCANNING;OPTIC/ATOMIC FORCE;MICROSCOPE;NEAR-FIELD'}, 'updated_ts': {'S': '1463469216387'}}}}, {'PutRequest': {'Item': {'created_ts': {'S': '1463469216387'}, u'label_cn': {'S': u'\u677f\u576f;\u6df7\u51dd\u571f\u697c\u677f;\u5efa\u8bbe;\u79fb\u52a8\u5f0f'}, u'patent_id': {'S': u'00000c08-958a-4385-923d-1d8a427fe1ca'}, 'version': {'N': '1'}, u'label_en': {'S': u'BUILDING;TRANSPORTABLE;SLAB;CONCRETE FLOOR'}, 'updated_ts': {'S': '1463469216387'}}}}, {'PutRequest': {'Item': {'created_ts': {'S': '1463469216387'}, u'label_cn': {'S': u'\u6811\u8102;\u94a2\u677f;\u963b\u5c3c'}, u'patent_id': {'S': u'00000ca4-43a2-42dd-b731-5ef0d409df11'}, 'version': {'N': '1'}, u'label_en': {'S': u'STEEL PLATE;DAMPING;RESIN'}, 'updated_ts': {'S': '1463469216387'}}}}, {'PutRequest': {'Item': {'created_ts': {'S': '1463469216387'}, 'version': {'N': '1'}, 'updated_ts': {'S': '1463469216387'}, u'label_cn': {'S': u'\u63a7\u5236;\u9ad8\u6548;\u5236\u52a8;\u5ba2\u8f66;\u56de\u6536;\u7535\u52a8;\u80fd\u91cf'}, u'patent_id': {'S': u'00000caa-d051-4cf1-83dc-f74636877a03'}}}}, {'PutRequest': {'Item': {'created_ts': {'S': '1463469216387'}, u'label_cn': {'S': u'\u5f52\u96f6;\u81ea\u52a8;\u7535\u8def;\u7535\u8bdd\u4f1a\u8bae'}, u'patent_id': {'S': u'00000cde-fbac-4eaa-8086-5e39995c70df'}, 'version': {'N': '1'}, u'label_en': {'S': u'TELECONFERENCING;AUTOMATIC;NULLING;CIRCUIT'}, 'updated_ts': {'S': '1463469216387'}}}}, {'PutRequest': {'Item': {'created_ts': {'S': '1463469216387'}, u'label_cn': {'S': u'\u673a\u5668;\u7f1d\u7eab'}, u'patent_id': {'S': u'00000ceb-83e2-4f34-af36-7d76fa491911'}, 'version': {'N': '1'}, u'label_en': {'S': u'MACHINE;SEWING'}, 'updated_ts': {'S': '1463469216387'}}}}, {'PutRequest': {'Item': {'created_ts': {'S': '1463469216387'}, u'label_cn': {'S': u'\u7403\u5458;\u89c6\u9891CD'}, u'patent_id': {'S': u'00000d00-2d6f-4cdb-b3d2-f6ff61291b55'}, 'version': {'N': '1'}, u'label_en': {'S': u'PLAYER;VIDEO CD'}, 'updated_ts': {'S': '1463469216387'}}}}, {'PutRequest': {'Item': {'created_ts': {'S': '1463469216387'}, u'label_cn': {'S': u'\u6db2\u6676;\u7535\u5b50\u8bbe\u5907'}, u'patent_id': {'S': u'00000d69-612f-4d32-9c0c-7a48cbf60633'}, 'version': {'N': '1'}, u'label_en': {'S': u'LIQUID CRYSTAL;ELECTRONIC;DISPLAY'}, 'updated_ts': {'S': '1463469216387'}}}}, {'PutRequest': {'Item': {'created_ts': {'S': '1463469216387'}, u'label_cn': {'S': u'\u53d7\u4f53\u6fc0\u52a8\u5242;\u975e\u5438\u6e7f\u76d0'}, u'patent_id': {'S': u'00000d8c-e9c9-4d5b-847d-2f82c08da2c4'}, 'version': {'N': '1'}, u'label_en': {'S': u'5-HT2C AGONIST;NON-HYGROSCOPIC SALT'}, 'updated_ts': {'S': '1463469216387'}}}}, {'PutRequest': {'Item': {'created_ts': {'S': '1463469216387'}, u'label_cn': {'S': u'\u53d7\u4f53\u6fc0\u52a8\u5242;\u975e\u5438\u6e7f\u76d0'}, u'patent_id': {'S': u'00000d8c-e9c9-4d5b-847d-2f82c08da2c4'}, 'version': {'N': '1'}, u'label_en': {'S': u'5-HT2C AGONIST;NON-HYGROSCOPIC SALT'}, 'updated_ts': {'S': '1463469216387'}}}}]}
ss = {'landscape_preprocess_test': [{'PutRequest': {'Item': {'created_ts': {'S': '1463471705516'}, u'label_cn': {'S': u'\u5305\u88c5;\u96c6\u88c5\u7bb1;\u5b9a\u671f\u7684\u6570\u7ec4;\u6587\u7ae0'}, u'patent_id': {'S': u'0000264a-84ea-414c-8242-8caedf228418'}, 'version': {'N': '1'}, u'label_en': {'S': u'ARTICLE;PACKING;CONTAINER;REGULAR ARRAY'}, 'updated_ts': {'S': '1463471705516'}}}}, {'PutRequest': {'Item': {'created_ts': {'S': '1463471705516'}, u'label_cn': {'S': u'\u70b9\u80f6\u673a;\u52a0\u70ed'}, u'patent_id': {'S': u'00002743-33f3-484b-be68-70a507c16243'}, 'version': {'N': '1'}, u'label_en': {'S': u'MACHINE;HEATING;DISPENSING'}, 'updated_ts': {'S': '1463471705516'}}}}, {'PutRequest': {'Item': {'created_ts': {'S': '1463471705516'}, 'version': {'N': '1'}, u'label_en': {'S': u'MACHINE;HEATING;DISPENSING'}, 'updated_ts': {'S': '1463471705516'}, u'patent_id': {'S': u'00002743-33f3-484b-be68-70a507c16243'}}}}, {'PutRequest': {'Item': {'created_ts': {'S': '1463471705516'}, u'label_cn': {'S': u'\u8f66\u8f86\u60ac\u67b6;\u94fe\u63a5'}, u'patent_id': {'S': u'0000274b-4010-4070-aeb9-6b7018c88189'}, 'version': {'N': '1'}, u'label_en': {'S': u'VEHICLE SUSPENSION;LINKED;AIR BAG'}, 'updated_ts': {'S': '1463471705516'}}}}, {'PutRequest': {'Item': {'created_ts': {'S': '1463471705516'}, u'label_cn': {'S': u'\u5fc3\u810f;\u969c\u5bb3;\u6cbb\u7597\u5242;\u56db\u7ea7;\u5236\u6cd5;\u5316\u5408\u7269;\u8111\u8840\u7ba1;\u75be\u75c5'}, u'patent_id': {'S': u'000027fa-69c2-459f-a360-90631f8c42b5'}, 'version': {'N': '1'}, u'label_en': {'S': u'QUATERNARY AMMONIUM;PRODUCING;COMPOUND'}, 'updated_ts': {'S': '1463471705516'}}}}, {'PutRequest': {'Item': {'created_ts': {'S': '1463471705516'}, u'label_cn': {'S': u'\u8bb0\u5f55\u6750\u6599'}, u'patent_id': {'S': u'00002851-0d00-4a2c-9d7e-6de66e38591f'}, 'version': {'N': '1'}, u'label_en': {'S': u'RECORD MATERIAL'}, 'updated_ts': {'S': '1463471705516'}}}}, {'PutRequest': {'Item': {'created_ts': {'S': '1463471705516'}, u'label_cn': {'S': u'\u690d\u7269;\u4f53\u79ef;\u9020\u7c92\u7684\u6750\u6599;\u9ad8\u538b\u91dc'}, u'patent_id': {'S': u'0000288f-e809-49eb-8fb2-5813226045ea'}, 'version': {'N': '1'}, u'label_en': {'S': u'BULKY MASS;PLANT;AUTOCLAVE;PELLETIZED MATERIAL'}, 'updated_ts': {'S': '1463471705516'}}}}, {'PutRequest': {'Item': {'created_ts': {'S': '1463471705516'}, u'label_cn': {'S': u'\u751f\u4ea7;\u98df\u54c1\u6750\u6599;\u4e73\u5316\u80fd\u529b'}, u'patent_id': {'S': u'000028ef-0d77-47d3-85ad-b81b120cdcaf'}, 'version': {'N': '1'}, u'label_en': {'S': u'EMULSIFICATION ABILITY;FOOD MATERIAL;PRODUCING'}, 'updated_ts': {'S': '1463471705516'}}}}, {'PutRequest': {'Item': {'created_ts': {'S': '1463471705516'}, u'label_cn': {'S': u'\u590d\u65b9;\u78e8\u5177'}, u'patent_id': {'S': u'00002913-1004-48ea-84ff-d9c38f2ee577'}, 'version': {'N': '1'}, u'label_en': {'S': u'ABRASIVE TOOL;COMPOUND'}, 'updated_ts': {'S': '1463471705516'}}}}, {'PutRequest': {'Item': {'created_ts': {'S': '1463471705516'}, u'label_cn': {'S': u'\u6728\u5730\u677f;\u590d\u5408'}, u'patent_id': {'S': u'00002924-5c83-432f-88f6-5693b3fba0e4'}, 'version': {'N': '1'}, u'label_en': {'S': u'COMPOSITE;WOODEN FLOOR'}, 'updated_ts': {'S': '1463471705516'}}}}]}


def get_proccesd_file_list(log_name_collection):

    cmd = ''' grep -r Processing %s |awk -F'/'  '{print $3}'| awk -F' ' '{print $1}' ''' %log_name_collection
    status, output = commands.getstatusoutput(cmd)
    processed_file_set = set(output.split())
    processed_file_list = list(processed_file_set)

    return processed_file_list


def choice_a_unprocessed_file(processed_file_list, unprocessed_file_list, even_flag):

    filename = None
    while True:

        if not unprocessed_file_list:
            return None

        filename = random.choice(unprocessed_file_list)

        num = int(filename.split('.')[0][1:])

        num_even_or_not = (num%2 == 0)

        if num_even_or_not == even_flag:  # even number
            if filename in processed_file_list:
                unprocessed_file_list.remove(filename)

                print "processed file", filename
                continue

            else:
                processed_file_list.append(filename)
                unprocessed_file_list.remove(filename)
                print "unprocessed file", filename
                break

        else:
            unprocessed_file_list.remove(filename)
            print "filtered file", filename

            continue

    return filename



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



def get_process_complete_file(dir):
    cmd = "cd  %s; wc -l * | grep x " %dir

    file_list = []
    status, output = commands.getstatusoutput(cmd)
    items = output.split("\n")
    print items
    for item in items:
        item = item.strip()
        num, filename = item.split()

        if eval(num) == 2051:
            file_list.append(filename)

    return file_list


if __name__ == '__main__':
    # get_process_complete_file("log_tmp")

    print str(ss)
    client = boto3.client('dynamodb')
    print client.scan(TableName='landscape_feature')

    item = {'label': {'S': 'test'}, 'patent_id': {'S': '0da01701-a555-4980-9e9c-9bb1a2bef35'} }

    client.put_item(TableName='landscape_feature', Item=item)


    # processed_file_list = get_proccesd_file_list("./logs")
    #
    # unprocessed_file_list = ["x47.text",'x9011.text', 'x41.text', 'x9007.text','x9012.text', 'x111.text', 'x9037.text']
    #
    #
    #
    # while True:
    #     filename = choice_a_unprocessed_file(processed_file_list, unprocessed_file_list, False)
    #
    #     if filename:
    #         print filename
    #     else:
    #         break


    # pid_labels = load_label("x41.text", None)
    # print pid_labels
    #
    # pids = set()
    # for item in pid_labels:
    #     pids.add(item["patent_id"])
    #
    # print len(pids)
