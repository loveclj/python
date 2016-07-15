#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: binmap.py
@time: 7/14/16 1:27 PM
"""

import feature.chemical_feature as ft
import feature.init_codebook as init
import train.bmu as bmu
import train.cluster_similarity as cluster_similarity
import distance

if __name__ == '__main__':
    row = 200
    som_x = 10
    som_y = 10
    dimenssion = 881
    feature_file_name = "./data/chemical_data.text"
    cid, matrix = ft.get_feature_matrix_from_file(feature_file_name, row)
    code_book = init.random_bin_init_codebook(som_x=som_x, som_y=som_y, dimenssion=dimenssion)

    for i in range(10):
        print "===== epoch ", i, "======"
        print distance.tanimoto.bin_tanimoto_similarity(matrix[2], code_book[2])
        bmus = bmu.find_bmu(code_book, matrix)
        for k, v in bmus.items():
            print k, v

        code_book = bmu.update_code_book(som_x, som_y, bmus, matrix, code_book)

    print "++++"
    bmus = bmu.find_bmu(code_book, matrix)


    for i in range(10):
        print "===== epoch ", i, "======"
        print distance.tanimoto.bin_tanimoto_similarity(matrix[2], code_book[2])
        bmus = bmu.find_bmu(code_book, matrix)
        for k, v in bmus.items():
            print k, v

        code_book = bmu.update_code_book2(som_x, som_y, bmus, matrix, code_book)

    print "++++"
    bmus = bmu.find_bmu(code_book, matrix)
    for k, v in bmus.items():
            print k, v

    print cluster_similarity.cluster_similarity(matrix, bmus, code_book)

    print distance.tanimoto.bin_tanimoto_similarity(matrix[4], matrix[48])

    test_bmu  = {}
    test_bmu[0] = range(row)
    print test_bmu
    print cluster_similarity.cluster_similarity(matrix, test_bmu, code_book)

    max = 0
    id = 0
    i = 0
    for v in matrix:
        s = distance.tanimoto.bin_tanimoto_similarity(matrix[99], v)

        if abs(s - 1) >= 0.0001 and s > max:

            max = s
            id = i

        i += 1

    print max
    print id






