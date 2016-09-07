#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: fingerprint_info.py
@time: 7/19/16 1:48 PM
"""

import math


def information_in_bit(p, threshold=0.001):
    if abs(p) < threshold or abs(1-p) < threshold:
        return 0
    else:
        info = p * math.log(p, 2) + (1 - p) * math.log(1 - p, 2)
        info *= -1
        return info


def importance_of_index(p, thres=0.001):
    # if p < thres:
    #     p = thres

    v = (1 - p) * p

    if v < thres:
        v = thres

    return -1 * math.log(v, 2)


def idf(p, thres=2**(-10)):
    if p < thres:
        p = thres

    return -1 * math.log(p, 2)


if __name__ == '__main__':

    out_fd = open('./id_info.text', 'w')
    with open("./text_process/id_freq_describe_sorted.text", "r") as fd:
        while True:
            line = fd.readline()
            if not line:
                break

            id, p, descr = line.strip('\n').split(':')[:3]
            print id, information_in_bit(float(p)), descr

            # importance = str(information_in_bit(float(p)))
            importance = str(importance_of_index(float(p)))
            # importance = str(idf(float(p)))
            line = id + ':' + importance + ":" + descr + '\n'
            out_fd.write(line)

    out_fd.close()


    print information_in_bit(0.2)
    print importance_of_index(0.000000000002)