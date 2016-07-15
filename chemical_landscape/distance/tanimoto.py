#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: tanimoto.py
@time: 7/14/16 1:28 PM
"""


def tanimoto_similarity(s1, s2, demenssion=881):
    n1 = 0
    n2 = 0
    union = 0
    for i in range(demenssion):
        if s1[i] == '1':
            n1 += 1

        if s2[i] == '1':
            n2 += 1

        if s1[i] == '1' or s2[i] == '1':
            union += 1

    return float(n1 + n2 - union)/union


def bin_tanimoto_similarity(vec1, vec2):
    dimession = len(vec1)
    vec1_no_zero_num = sum(vec1)
    vec2_no_zero_num = sum(vec2)
    comm_no_zero_num = 0
    for i in range(dimession):
        if vec1[i] == 1 and vec2[i] == 1:
            comm_no_zero_num += 1

    return float(comm_no_zero_num)/(vec1_no_zero_num + vec2_no_zero_num - comm_no_zero_num)


if __name__ == '__main__':
    pass