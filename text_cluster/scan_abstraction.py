#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: scan_abstraction.py
@time: 6/15/16 11:59 AM
"""

from dynamodb import batch_get
from dynamodb import extract_field
from fileIO import dumps


if __name__ == '__main__':

    table_name = 'patent_abstract'
    fields = 'abstract,patent_id,lang'
    fields_list = ['abstract', 'patent_id', 'lang']
    field_type = {'abstract': 'B', "patent_id": "S", "lang": "S"}

    ''' load patent list from file patent2tilte '''
    title_file = "./data/title.text"
    patent2title = dumps.load_map_from_file(title_file)
    patent_list = patent2title.keys()

    ''' filter other lang '''
    lang = "EN"
    batch_count = 50

    patent_count = len(patent_list)
    write_count = 0

    server = batch_get.BatchGet(table_name=table_name, fields=fields_list, max_batch_count=50)

    start = 0
    end = 0

    field_type = {'abstract': 'B', "patent_id": "S", "lang": "S"}
    while start < patent_count:

        end = min(start + batch_count, patent_count)

        key_list = []
        for patent in patent_list[start: end]:
            key = {'patent_id': {'S': patent}, 'lang': {'S': lang}}
            key_list.append(key)

        response = server.batch_get_once(key_list)

        if not response:
            continue

        response_items = response['Responses']['patent_abstract']
        field_values = extract_field.extract_fields_from_item_list(response_items, field_type)

        i = 0
        patent2abstract = {}
        for abstract in field_values['abstract']:
            patent = field_values['patent_id'][i]
            patent2abstract[patent] = abstract.replace("\n", " ")

            i += 1

        write_count += dumps.dump_map_to_file(patent2abstract, "./data/abstract.text", "a")

        print "write count:", write_count

        start += batch_count
