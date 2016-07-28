#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: similarity.py
@time: 7/25/16 5:39 PM
"""


def tanimoto_similarity(vec1, vec2):
    dimession = len(vec1)
    vec1_no_zero_num = sum(vec1)
    vec2_no_zero_num = sum(vec2)
    comm_no_zero_num = 0
    for i in range(dimession):
        if vec1[i] == 1 and vec2[i] == 1:
            comm_no_zero_num += 1

    return float(comm_no_zero_num)/(vec1_no_zero_num + vec2_no_zero_num - comm_no_zero_num)


def importance_similarity(vec1, vec2, weight):
    dimession = len(vec1)
    vec1_importance = 0
    vec2_importance = 0
    for i in range(dimession):
        vec1_importance += weight[i] * vec1[i]
        vec2_importance += weight[i] * vec2[i]

    comm_importance = 0
    for i in range(dimession):
        if vec1[i] == 1 and vec2[i] == 1:
            comm_importance += weight[i]

    return float(comm_importance)/(vec1_importance + vec2_importance - comm_importance)


def generate_feature_matrix(file_name):
    matrix = {}
    with open(file_name, 'r') as fd:
        while True:
            line = fd.readline()
            if not line:
                break

            cid, fingerprint = line.strip('\n').split(',')
            f = []
            for e in fingerprint:
                f.append(int(e))

            matrix[cid] = f

    return matrix


if __name__ == '__main__':

    fd = open('../chemical_landscape/id_info.text', 'r')
    weight = [0]*881
    while True:
        line = fd.readline()
        if not line:
            break

        id, w = line.split(':')[:2]
        weight[int(id)] = float(w)
        # print w

    feature_file_name = 'feature.text'
    m = generate_feature_matrix(feature_file_name)

    for k, v in m.items():
        print '-----'
        print k, importance_similarity(v, m['2'], weight)
        print k, tanimoto_similarity(v, m['2'])

    i = 0
    for k in m['1']:
        if k:
            print i,

        i += 1

    print


    i = 0
    for k in m['2']:
        if k:
            print i,

        i += 1
    print

    i = 0
    for k in m['3']:
        if k:
            print i,

        i += 1
    print

    i = 0
    for k in m['4']:
        if k:
            print i,

        i += 1
    print
