#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: dumps.py
@time: 6/14/16 5:13 PM
"""


import codecs


def dump_map_to_file(dic, filename, mode="w"):
    write_count = 0
    with codecs.open(filename=filename, mode=mode, encoding="utf-8") as fd:
        for k, v in dic.items():
            if type(k) != str:
                k = str(k)

            if type(v) != str:
                v = str(v)

            try:

                line = k + u":" + v + u'\n'
                fd.write(line)
                write_count += 1
            except:
                pass
                # print k
                # print v

    return write_count


def dump_tuple_list_to_file(tuple_list, filename, mode="w"):
    write_count = 0
    with codecs.open(filename=filename, mode=mode, encoding="utf-8") as fd:
        for item in tuple_list:
            line = ""
            for e in item:
                if type(e) != str:
                    e = str(e)
                line += e + u","

            line += u'\n'

            fd.write(line)
            write_count += 1

    return write_count


def load_map_from_file(filename, delimiter=':'):
    kv ={}
    with codecs.open(filename=filename, mode='r', encoding='utf-8') as fd:
        while True:
            line = fd.readline().strip('\n')

            ''' read EOF '''
            if not line:
                break

            try:
                key, value = line.split(delimiter)

                kv[key] = value

            except:
                continue

    return kv


def print_map(dict):
    for k, v in dict.items():
        print k, v


if __name__ == '__main__':
    pass