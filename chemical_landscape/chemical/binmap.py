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
    som_x = 8
    som_y = 8
    dimenssion = 881

    feature_file_name = "chemical_data_10k.text"
    cid, matrix = ft.get_feature_matrix_from_file(feature_file_name, row)
    code_book = init.random_bin_init_codebook(som_x=som_x, som_y=som_y, dimenssion=dimenssion)

    total_epoch = 10
    for i in range(total_epoch):
        print "===== epoch ", i, "======"
        print distance.tanimoto.bin_tanimoto_similarity(matrix[2], code_book[2])
        bmus = bmu.find_bmu(code_book, matrix)
        for k, v in bmus.items():
            print k, v

        ''' radius of neighborhood, decrease with epoch '''
        radius = min(som_x, som_y)/2 * (1 - float(i) / total_epoch)

        radius = int(radius)

        ''' update code book '''
        code_book = bmu.update_code_book(som_x, som_y, bmus, matrix, code_book, radius)

    bmus = bmu.find_bmu(code_book, matrix)
    for k, v in bmus.items():
            print k, v

    print "average similarity of each grid"
    print cluster_similarity.cluster_similarity(matrix, bmus, code_book)

    print "average tanimoto similarity of all feature"
    print cluster_similarity.cluster_similarity(matrix, {0: range(row)}, code_book)[0]








