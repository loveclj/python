#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: cluster_similarity.py
@time: 7/14/16 5:28 PM
"""

import sys
sys.path.append("..")

import distance.tanimoto as tanimoto


def cluster_similarity(matrix, bmus, code_book):
    cs = []
    for i in range(len(code_book)):
        if i not in bmus.keys():
            cs.append("None")
            continue

        if len(bmus[i]) == 1:
            cs.append(1)
            continue

        sum_similarity = 0
        items = bmus[i]
        for j in range(len(items) - 1):
            for k in range(j + 1, len(items)):
                sum_similarity += tanimoto.bin_tanimoto_similarity(matrix[items[j]], matrix[items[k]])

        cs.append(sum_similarity*2/(len(items) * (len(items)-1)))

    return cs


if __name__ == '__main__':
    pass