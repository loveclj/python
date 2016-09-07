#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: svd_normal.py
@time: 9/7/16 10:28 AM
"""


from sklearn.decomposition import TruncatedSVD
from sklearn.decomposition import PCA

import numpy as np


if __name__ == '__main__':
    matrix = [[1, 2, 3, ], [4, 5, 6] ]
    matrix = np.array(matrix)
    # svd = TruncatedSVD(n_components=2)
    # svd.fit(matrix)
    # print svd.explained_variance_ratio_

    print matrix.shape
    symmetric_matrix = np.dot(np.transpose(matrix), matrix)
    print
    symmetric_matrix2 = np.dot(matrix, np.transpose(matrix))


    # pca = PCA(n_components=2)
    # pca.fit(symmetric_matrix)
    # print pca.explained_variance_
    # print symmetric_matrix
    v = np.linalg.eig(symmetric_matrix)
    print v

    # print np.dot(matrix, v1[1])
    # print v1
    print np.linalg.eig(symmetric_matrix2)

    s = np.linalg.svd(matrix)
    #
    print s
    # print np.linalg.svd(np.transpose(matrix))
    #z
    print np.dot(np.dot(s[0], np.diag(v=s[1])), np.transpose(v[1][:, 0:2]))

    print  np.transpose(v[1][:, 0:2])
    #
    # print np.dot(matrix, np.transpose(s[2]))

    # print np.product(s[0], s[1])
