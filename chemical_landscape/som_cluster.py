#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: som_cluster.py
@time: 7/7/16 5:59 PM
"""

from mvpa2.suite import SimpleSOMMapper# pl
import numpy as np
import matplotlib.pyplot as plt


def get_feature_from_file(filename, N):
    fp = open(filename, 'w')
    fingerprint_list = []
    cid_list = []
    item_count = 0
    while True:
        line = fp.readline()
        if not line:
            break

        item_count += 1

        cid, fingerprint = line.split(',')
        feature = []
        for f in fingerprint:
            feature.append(int(f))

        cid_list.append(cid)
        fingerprint_list.append(feature)

    return cid_list, fingerprint_list


if __name__ == '__main__':
    N = 100
    cid_list, feature_list = get_feature_from_file('chemical_data.text', N)

    feature_matrix = np.array(feature_list)
    som = SimpleSOMMapper((20, 20), 400, learning_rate=0.05)
    som.train()
    plt.imshow(som.K, origin='lower')