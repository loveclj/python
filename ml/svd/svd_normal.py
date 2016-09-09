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
import cv2


import numpy as np


def svd_n_compontents(s, n):
    u = s[0][:, 0:n]
    e = np.diag(s[1][0:n])
    v = np.transpose(s[2])[:, 0:n]
    return np.dot(np.dot(u, e), v.transpose()).astype('uint8')  # TODO data type of matrix is uint8

if __name__ == '__main__':

    img = cv2.imread("/home/lizhifeng/Desktop/cat.jpg")

    print type(img)
    for i in range(3):
        svd_result = np.linalg.svd(img[:, :, i])

        n_compontents_img = svd_n_compontents(svd_result, 150)

        img[:, :, i] = n_compontents_img

    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



    svd = TruncatedSVD(n_components=2)
    svd.fit(img)
    print svd.explained_variance_ratio_
    #
    # cv.imread("~/Desktop/cat.jpg")
    #
    # print matrix.shape
    # symmetric_matrix = np.dot(np.transpose(matrix), matrix)
    # print
    # symmetric_matrix2 = np.dot(matrix, np.transpose(matrix))
    #
    #
    # # pca = PCA(n_components=2)
    # # pca.fit(symmetric_matrix)
    # # print pca.explained_variance_
    # # print symmetric_matrix
    # v = np.linalg.eig(symmetric_matrix)
    # print v
    #
    # # print np.dot(matrix, v1[1])
    # # print v1
    # print np.linalg.eig(symmetric_matrix2)
    #
    # s = np.linalg.svd(matrix)
    # #
    # print s
    # # print np.linalg.svd(np.transpose(matrix))
    # #
    # print np.dot(np.dot(s[0], np.diag(v=s[1])), np.transpose(v[1][:, 0:2]))
    #
    # print np.transpose(v[1][:, 0:2])
    # #
    # # print np.dot(matrix, np.transpose(s[2]))
    #
    # # print np.product(s[0], s[1])
