#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: file_read.py.py
@time: 2/3/16 2:35 PM
"""

import numpy as np


def load_file(filename):
    with open(filename, "r") as fd:
        lines = fd.readlines()
        return lines

def extract_feature_label(lines):
    features = []
    labels = []
    for line in lines:
        feature_str = line.strip("\n").split(',')
        feature_list = []
        for f in feature_str[:-1]:
            feature_list.append(float(f))

        labels.append(feature_str[-1])
        features.append(feature_list)

    features = np.array(features)

    return features, labels


if __name__ == '__main__':
    lines = load_file("iris.data")
    extract_feature_label(lines)
