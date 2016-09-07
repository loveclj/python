#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: tanimoto.py
@time: 7/14/16 1:28 PM
"""


def tanimoto_similarity(vec1, vec2):

    dimenssion = len(vec1)

    vec1_no_zero_num = vec1.sum()
    vec2_no_zero_num = vec2.sum()

    comm_no_zero_num = 0
    for i in range(dimenssion):
        if vec1[i] == vec2[i]:
            comm_no_zero_num += vec1[i]

    return float(comm_no_zero_num)/(vec1_no_zero_num + vec2_no_zero_num - comm_no_zero_num)
    # return vec2_no_zero_num
def hamming_distance(vec1, vec2):

    d = 0
    dimension = len(vec1)
    for i in range(dimension):
        if vec1[i] != vec2[i]:
            d += 1

    return d


def cluster_similarity(matrix, bmus, code_book):
    cs = []

    som_grid_count = code_book.shape[0]
    for grid_id in range(som_grid_count):

        ''' empty grid, no data vector matched '''
        if grid_id not in bmus.keys():
            cs.append("None")
            continue

        ''' only one data vector matched '''
        if len(bmus[grid_id]) == 1:
            cs.append(1)
            continue

        sum_similarity = 0
        items = bmus[grid_id]
        item_count = len(items)
        for i in range(item_count - 1):
            for j in range(i + 1, item_count):
                sum_similarity += tanimoto_similarity(matrix[items[i]], matrix[items[j]])

        cs.append(sum_similarity*2/(item_count * (item_count-1)))

    return cs


if __name__ == '__main__':
    a = [1, 0, 1]
    b = [1, 1, 0]
    print hamming_distance(a, b)