#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: tanimoto.py
@time: 7/14/16 1:28 PM
"""


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