#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: binary_pca.py
@time: 9/8/16 1:59 PM
"""

import numpy as np
from sklearn.decomposition import PCA
import cv2


def load_matrix_from_file(filename, n, index=1):
    matrix = []
    count = 0
    for line in open(filename):
        f = line.strip('\n').split(',')[index]
        vec = []
        for i in f:
            vec.append(int(i))
        matrix.append(vec)
        count += 1
        if count == n:
            break

    return np.array(matrix)


if __name__ == '__main__':
    matrix = load_matrix_from_file('../../data/chemical_data.text', 10000000)
    # matrix = load_matrix_from_file(filename='/home/lizhifeng/cuda-workspace/Binary_SOM/name_formula_fingerprint_3k.text',
    #                                n=2000000, index=2)

    # print matrix.astype('uint8').dtype
    # print matrix

    # cv2.imshow('image', matrix.astype('uint8')*255)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # np.linalg.eigvals(matrix.transpose().dot(matrix)).shape
    # print np.linalg.svd(matrix)

    # print
    # pca = PCA(n_components=1)
    # pca.fit(matrix)
    #
    # print pca.explained_variance_ratio_.shape
    # print pca.components_.shape
    # print pca.noise_variance_

    a =  matrix.sum(axis=0)
    c = (a == 0)
    print c.sum()
    # print a.sum()