#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: scan_biblio.py
@time: 6/15/16 4:41 PM
"""

from dynamodb import batch_get
import codecs
from fileIO import dumps
import json


if __name__ == '__main__':

    table_name = 'patent_biblio'
    fields = 'patent_id,assignee,inventor,pbdt,family_inpadoc,family_original'
    # fields_list = ['patent_id', 'assignee', 'inventor', 'pbdt', 'family_inpadoc', 'family_original']
    fields_list = ['patent_id', 'ipc', 'ipcr']
    ''' load patent list from file patent2tilte '''
    title_file = "./data/title.text"
    patent2title = dumps.load_map_from_file(title_file)
    patent_list = patent2title.keys()

    ''' filter other lang '''
    batch_count = 50

    patent_count = len(patent_list)
    write_count = 0

    server = batch_get.BatchGet(table_name=table_name, fields=fields_list, max_batch_count=50)

    start = 0
    end = 0

    fd = codecs.open(filename="./data/ipc.text", mode="a", encoding='utf-8')
    # fd.write("[\n")
    while start < patent_count:

        end = min(start + batch_count, patent_count)

        key_list = []
        for patent in patent_list[start: end]:
            key = {'patent_id': {'S': patent}}
            key_list.append(key)

        response = server.batch_get_once(key_list)

        if not response:
            continue

        response_items = response['Responses'][table_name]

        for item in response_items:
            # line = json.dumps(obj=item, indent=True, encoding='utf-8', ensure_ascii=False) + "," + "\n"
            # print line
            patent = item['patent_id']["S"]
            ipc_set = set()

            ipc_map_list = []
            if 'ipc' in item.keys():
                ipc_map_list.extend(item['ipc']['L'])

            if 'ipcr' in item.keys():
                ipc_map_list.extend(item['ipcr']['L'])

            for m in ipc_map_list:
                try:
                    ipc = m['M']['code']['M']['full']['S']
                    ipc_set.add(ipc)
                except:
                    pass

            if not ipc_set:
                continue

            line = patent + u":" + u",".join(ipc_set) + "\n"
            fd.write(line)

        start += batch_count

    # fd.write("]\n")
    fd.close()
