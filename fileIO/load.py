#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: load.py
@time: 6/16/16 5:33 PM
"""


import codecs


def load_list_from_file(filename):
    l = []
    with codecs.open(filename=filename, mode='r', encoding='utf-8') as fd:
        while True:
            line = fd.readline().strip('\n')
            if not line:
                break

            l.append(line)

    return l


def load_list_list_from_file(filename):
    list_list = []
    with codecs.open(filename=filename, mode="r", encoding='utf-8') as fd:
        while True:
            line =  fd.readline().strip('\n')
            if not line:
                break

            e = line.replace(',', ':').split(':')
            list_list.append(e)

    return list_list


if __name__ == '__main__':
    pass