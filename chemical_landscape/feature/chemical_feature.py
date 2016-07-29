#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: chemical_feature.py
@time: 7/14/16 1:39 PM
"""
import numpy as np


def get_feature_matrix_from_file(file_name, N):

    fingerprint_list = []
    cid_list = []
    item_count = 0

    for line in open(file_name):

        cid, fingerprint = line.strip('\n').split(',')
        feature = []

        for f in fingerprint:
            feature.append(int(f))

        cid_list.append(cid)
        fingerprint_list.append(feature)

        item_count += 1
        if N == item_count:
            break

    return np.array(cid_list), np.array(fingerprint_list)


if __name__ == '__main__':
    cids, mat = get_feature_matrix_from_file("../chemical_data_10k", 100)
    print cids[1]
    print mat[0].sum()
    k = mat[0] * mat[1]
    print k.sum()

    comm = 0
    for i in range(881):
        comm += mat[0][i] * mat[1][i]

    print comm




