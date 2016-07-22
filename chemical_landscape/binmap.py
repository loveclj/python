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
import math

if __name__ == '__main__':
    row = 5000
    som_x = 10
    som_y = 10
    dimenssion = 881

    feature_file_name = "./data/chemical_data.text"
    cid, matrix = ft.get_feature_matrix_from_file(feature_file_name, row)
    code_book = init.random_bin_init_codebook(som_x=som_x, som_y=som_y, dimenssion=dimenssion)

    weight = [0] * dimenssion
    with open('id_info.text', 'r') as fd:
        while True:
            line = fd.readline()
            if not line:
                break

            id, p = line.split(':')[:2]
            id = int(id)
            p = float(p)
            weight[id] = p


    total_epoch = 10

    result_pre = None
    for i in range(total_epoch):
      n = 0
      while True:

        n += 1
        if n >= 10:
            break

        print "===== epoch ", i, "======"
        print distance.tanimoto.importance_similarity(matrix[2], code_book[2], weight)
        bmus = bmu.find_importance_bmu(code_book, matrix, weight)
        for k, v in bmus.items():
            print k, v

        ''' radius of neighborhood, decrease with epoch '''
        lambda_zero = min(som_x, som_y)/2

        radius = lambda_zero * math.pow(1.0 / lambda_zero, float(i) / total_epoch) - 1

        # radius = int(radius)

        ''' update code book '''
        code_book = bmu.update_code_book(som_x, som_y, bmus, matrix, code_book, radius)

        result_now = cluster_similarity.cluster_importance_similarity(matrix, bmus, code_book, weight)
        if result_now == result_pre:
            print "***** stable ****"
            break
        else:
            result_pre = result_now
            print "******** not stable ********"

    bmus = bmu.find_importance_bmu(code_book, matrix, weight)
    s = cluster_similarity.cluster_importance_similarity(matrix, bmus, code_book, weight)

    for k, v in bmus.items():
            print k, v, s[k]


    ''' average similarity of each grid '''

    ''' average tanimoto similarity of all feature vector '''
    print cluster_similarity.cluster_importance_similarity(matrix, {0: range(row)}, code_book, weight)



    right_num = 0
    same_cluster_num = 0
    for k, v in bmus.items():
        for j in v:
            id = 0
            dis = 0
            for i in range(row):
                now = distance.tanimoto.importance_similarity(matrix[i], matrix[j], weight)

                if now < 1 and now  > dis:
                    dis = now
                    id = i

            neighbors = []
            for c in range(som_x*som_y):
                if c in bmus.keys() and bmu.is_neighbor(som_x, som_y, k, c, 1.5):
                    neighbors.extend(bmus[c])

            if id not in neighbors:
                print j, id, k, neighbors
                print "best match feature is not neighbor"
            else:
                print "----------"
                right_num += 1

            if id in bmus[k]:
                same_cluster_num += 1

    print row
    print right_num
    print same_cluster_num











