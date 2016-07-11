#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: load_dict.py
@time: 5/30/16 4:10 PM
"""


import codecs
import json
import commands
import re


def load_dict_list_from_file(filename):
    term_dict_list = []
    with codecs.open(filename=filename, mode='r', encoding='utf-8') as fd:
        while True:
            line = fd.readline()
            if not line:
                break

            term_dict = json.loads(line.strip('\n'))

            term_dict_list.append(term_dict)

    return term_dict_list


def list_flie(mode):
    cmd = 'ls ' + mode
    status, output = commands.getstatusoutput(cmd)
    file_list = output.split()
    return file_list


if __name__ == '__main__':
    term_dict_list = load_dict_list_from_file(filename="./wipo_pearl/29_2903_TEXT.txt")

    file_list = list_flie("./wipo_pearl/*.txt")
    mode = re.compile(r'pretty')

    term_cnt = 0
    en_cn_dict = {}
    catagory = {}
    for file in file_list:
        if mode.findall(file):
            continue

        print file

        term_dict_list = load_dict_list_from_file(filename=file)

        try:
            for term_dict in term_dict_list:
                term_cnt += 1

                if term_dict[u'name'] not in catagory.keys():
                    catagory[term_dict[u'name']] = set()

                catagory[term_dict[u'name']].add(term_dict[u'child_name'])

                term = term_dict[u'term'][u'term_name']

                translation_list = term_dict[u'term'][u'translation']

                for t in translation_list:
                    if t[u'term_lang'] == u'ZH':
                        cn_term = t[u'term_name']

                        if term not in en_cn_dict.keys():
                            en_cn_dict[term] = []

                        en_cn_dict[term].append(cn_term)

        except:
            pass

    print term_cnt

    # for k in en_cn_dict.keys():
    #     if len(en_cn_dict[k]) >= 2:
    #         print k, ":",
    #         for cn_term in en_cn_dict[k]:
    #             print cn_term,
    #             # pass
    #
    #         print
    #
    # for k in catagory.keys():
    #     print k, ":",
    #     for child_catagory in catagory[k]:
    #         print child_catagory, "/",
    #     print