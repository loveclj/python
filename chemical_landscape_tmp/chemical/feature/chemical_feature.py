#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: chemical_feature.py
@time: 7/14/16 1:39 PM
"""


def get_feature_matrix_from_file(filename, N):
    fp = open(filename, 'r')
    fingerprint_list = []
    cid_list = []
    item_count = 0
    while True:
        line = fp.readline()
        if not line:
            break

        item_count += 1

        cid, fingerprint = line.strip('\n').split(',')
        feature = []

        for f in fingerprint:
            feature.append(int(f))

        cid_list.append(cid)
        fingerprint_list.append(feature)

        if N == item_count:
            break

    return cid_list, fingerprint_list


if __name__ == '__main__':
    pass