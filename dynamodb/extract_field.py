#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: extract_field.py
@time: 6/14/16 3:42 PM
"""


import string_gzip


def extract_fields_from_item_list(items, field_types):
    fields_list = field_types.keys()

    while u'' in fields_list:
        fields_list.remove('')

    field_value_list = {}
    for f in fields_list:
        field_value_list[f] = []

    for item in items:
        for f in fields_list:

                value = None
            # try:
                type = field_types[f]
                if type == "B":
                    value = string_gzip.decompress(item[f][type])
                else:
                    value = item[f][type]
            # except:
            #     value = None

                field_value_list[f].append(value)

    return field_value_list


if __name__ == '__main__':
    l = ['', 'a', '', 'b']
    l.remove('')
    print l