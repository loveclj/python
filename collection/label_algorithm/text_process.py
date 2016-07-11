#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: text_process.py.py
@time: 3/21/16 3:35 PM
"""

import aws_utility.dynamodb as dynamodb
import aws_utility.gzip_api as gzip
import term_frequence
import string_utility


def get_title_abstr_from_dynamodb(patents, title_table_name, abstr_table_name, lang="EN"):

    patent2title = {}
    patent2abstr = {}

    title_table = dynamodb.Table(table_name=title_table_name, partition_key='patent_id', sort_key='lang')
    abstr_table = dynamodb.Table(table_name=abstr_table_name, partition_key='patent_id', sort_key='lang')

    i = 0
    for patent in patents:
        try:
            title_binary = title_table.get_item(partition_key=patent, sort_key=lang)[u'Item'][u'title']
            title = gzip.decompress(title_binary)
            title = title.replace('\n', '.')
            if title is None:
                print "no title:", patent
            else:
                patent2title[patent] = title
        except:
            print "no title:", patent

        try:
            abstr_binary = abstr_table.get_item(partition_key=patent, sort_key=lang)[u'Item'][u'abstract']
            abstr = gzip.decompress(abstr_binary)
            abstr = abstr.replace('\n', '.')
            if abstr is None:
                print "no abstr:", patent
            else:
                patent2abstr[patent] = abstr
        except:
            print "no abstr:", patent


    return patent2title, patent2abstr


def save_title_abstr_to_text(patents, title_table_name, abstr_table_name, lang="EN", title_text='title', abstr_text='abstr'):

    patent2title, patent2abstr = get_title_abstr_from_dynamodb(patents, title_table_name, abstr_table_name, lang)

    title_fd = open(title_text, 'w')
    for patent in patent2title.keys():
        title_fd.writelines(patent+'\n')
        title_fd.writelines(patent2title[patent]+'\n')


    abstr_fd = open(abstr_text, 'w')
    for patent in patent2abstr.keys():
        abstr_fd.writelines(patent+'\n')
        abstr_fd.writelines(patent2abstr[patent]+'\n')

    title_fd.close()
    abstr_fd.close()


def load_tiltle_abstr_from_text(title_text='title', abstr_text='abstr'):

    title_fd = open(title_text, 'r')

    patent2title = {}
    lines = title_fd.readlines()
    patent_count = len(lines)/2
    i = 0
    while i < patent_count:
        patent = lines[2*i].strip('\n')
        title = lines[2*i+1].strip('\n')
        patent2title[patent] = title
        i += 1

    abstr_fd = open(abstr_text, 'r')

    patent2abstr = {}
    lines = abstr_fd.readlines()
    patent_count = len(lines)/2
    i = 0
    while i < patent_count:
        patent = lines[2*i].strip('\n')
        abstr = lines[2*i+1].strip('\n')
        patent2abstr[patent] = abstr
        i += 1

    return patent2title, patent2abstr


def get_stem_freq(patent2title, patent2abstr):
    patent2abstr_stem_freq = {}
    patent2title_stem_freq = {}
    title_stem_freq = {}
    abstr_stem_freq = {}

    stem2term = {}
    for patent, abstr in patent2abstr.items():
        words_list = string_utility.split_text(abstr)
        patent2abstr_stem_freq[patent] = term_frequence.get_stem_freq(words_list, stem2term, "EN")
        for stem, freq in patent2abstr_stem_freq[patent].items():
            if stem in abstr_stem_freq.keys():
                abstr_stem_freq[stem] += freq
            else:
                abstr_stem_freq[stem] = freq

    for patent, title in patent2title.items():
        words_list = string_utility.split_text(title)
        patent2title_stem_freq[patent] = term_frequence.get_stem_freq(words_list, stem2term, "EN")
        for stem, freq in patent2title_stem_freq[patent].items():
            if stem in title_stem_freq.keys():
                title_stem_freq[stem] += freq
            else:
                title_stem_freq[stem] = freq

    return patent2title_stem_freq, title_stem_freq, patent2abstr_stem_freq, abstr_stem_freq, stem2term


def save_dict(dictionary, filename):
    fd = open(filename, 'w')
    for k, v in dictionary.items():
        line = str(k) + " " + str(v) + '\n'
        fd.write(line)
    fd.close()


def save_dict_dict(dictionary, filename):
    fd = open(filename, 'w')
    for k, m in dictionary.items():
        fd.write(k)
        pair = ""
        for s, v in m.items():
            pair += " " + s + " " + str(v)

        fd.write(pair + '\n')


def load_dict(filename):
    fd = open(filename, 'r')
    lines = fd.readlines()
    dict = {}
    for line in lines:
        kv = line.strip('\n').split(" ")

        try:
            dict[kv[0]] = eval(kv[1])
        except:
            dict[kv[0]] = kv[1]

    fd.close()
    return dict


def load_dict_dict(filename):
    fd = open(filename, 'r')
    lines = fd.readlines()
    dict = {}
    for line in lines:
        words = line.strip('\n').split(" ")

        length = len(words)
        i = 1

        kv = {}
        while i < length:
            try:
                kv[words[i]] = eval(words[i+1])
            except:
                kv[words[i]] = words[i+1]
            i += 2

        dict[words[0]] = kv

    return dict


def load_list(filename="stopwords"):
    fd = open(filename, "r")
    lines = fd.readlines()
    words_list = []

    for line in lines:
        words_list.append(line.strip('\n'))

    words_set = set(words_list)
    return words_set






if __name__ == '__main__':
    patents = ['1986975f-d2e1-44de-b32f-29c8211586fe', '450573c3-8eac-4827-bd09-bb72459266f4']
    get_title_abstr_from_dynamodb(patents, title_table_name='patent_title', abstr_table_name='patent_abstr')