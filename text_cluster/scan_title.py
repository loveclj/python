#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: scan_title.py
@time: 6/14/16 5:10 PM
"""

from dynamodb import scan
from dynamodb import extract_field
from fileIO import dumps


if __name__ == '__main__':

    table_name = 'patent_title'
    fields = 'title,patent_id,lang'
    field_type = {'title': 'B', "patent_id": "S", "lang": "S"}

    ''' filter other lang '''
    lang = "EN"

    patent_count = 0
    write_count = 0
    N = 1000000

    scaner = scan.Scanner(table_name=table_name, fields=fields)

    while patent_count < N:
        patent2title = {}
        i = 0
        last_key, items = scaner.scan_once()

        field_values = extract_field.extract_fields_from_item_list(items, field_type)

        for title in field_values['title']:

            if field_values['lang'][i] == "EN":
                patent = field_values['patent_id'][i]
                patent2title[patent] = title
                patent_count += 1

            i += 1
        print "en patent count:", patent_count

        write_count += dumps.dump_map_to_file(patent2title, "./data/title.text", "a")

        print "write count:", write_count
