#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: binmap.py
@time: 7/14/16 1:27 PM
"""

import math
import numpy as np

import feature.chemical_feature as ft
import feature.init_codebook as init

import distance
import distance.bmu
import distance.dist
import random
import matplotlib.pyplot as plt


def load_weight_from_file(file_name):
    weight = [0] * dimenssion

    for line in open(file_name):

            id, p = line.split(':')[:2]
            id = int(id)
            p = float(p)
            weight[id] = p

    return np.array(weight)


if __name__ == '__main__':
    row = 15
    som_x = 5
    som_y = 5
    dimenssion = 881

    # feature_file_name = "chemical_data_10k"
    feature_file_name = "formula_figerprint.text"
    feature_file_name = "formula_figerprint_ali_data_set2.text"
    feature_file_name = "formula_figerprint_ali_suger_data.text"
    cid, matrix = ft.get_feature_matrix_from_file(feature_file_name, row)

    code_book = init.random_bin_init_codebook(som_x=som_x, som_y=som_y, dimenssion=dimenssion)

    weight = load_weight_from_file('id_info.text')
    # weight = [1] * dimenssion
    # weight = np.array(weight)



    matrix = matrix * weight
    code_book = code_book * weight


    total_epoch = som_x

    result_pre = None
    for i in range(total_epoch):

      max_train_times_per_epoch = 0
      radius = int(som_x/2 - i)

      if radius < 0:
          break


      while True:
        print "radius is", radius
        max_train_times_per_epoch += 1
        if max_train_times_per_epoch >= 10:
            break
            # pass

        print "===== epoch ", i, "======"

        bmus = distance.bmu.find_bmu(code_book, matrix)
        # for k, v in bmus.items():
        #     print k, v

        ''' radius of neighborhood, decrease with epoch '''
        lambda_zero = min(som_x, som_y)/2

        radius = lambda_zero * math.pow(1.0 / lambda_zero, float(i) / total_epoch) - 1

        # radius = int(radius)

        ''' update code book '''
        code_book = distance.bmu.update_code_book(som_x, som_y, bmus, matrix, code_book, radius, weight)

        result_now = distance.dist.cluster_similarity(matrix, bmus, code_book)

        if result_now == result_pre:
            print "***** stable ****"
            break
        else:
            result_pre = result_now
            print "******** not stable ********"

    bmus = distance.bmu.find_bmu(code_book, matrix)
    s = distance.dist.cluster_similarity(matrix, bmus, code_book)

    for k, v in bmus.items():
            print k, v, s[k]


    x_list = []
    y_list = []
    label_list = []

    re_fd = open("cluster_result.text", 'w')
    for k, v in bmus.items():
        line = 'cluster %d\n' %k
        re_fd.write(line)
        n = 1
        m = 0
        for i in v:
            x = k % som_x
            y = k / som_x
            # x_list.append(x + random.random()*0.9)
            # y_list.append(y + random.random()*0.9)

            x_list.append(x + 0.2*m + 0.1)
            y_list.append(y + 0.2 * n)

            m += 1

            n += int(m/5)
            print int(m/5), m
            m %= 5

            if n == 5:
                print "error"

            print i, cid[i]

            # label = None
            # i += 100
            # if i>= 100 and i<= 102:
            #     label = "1"
            # if i>=103 and i<= 107:
            #     label ="2"
            # if i>=108 and i <=110:
            #     label = "3"
            # if i>=111 and i<=117:
            #     label = "4"
            # if i>=118 and i<=124:
            #     label = "5"
            #
            #
            # if label != None:
            #     label += "," + str(i-100)
            #
            # i -= 100

            label = str(i)

            label_list.append(label)

            line = str(i) + "," + cid[i] + "\n"
            re_fd.write(line)


        re_fd.write('======================')

    print(x_list)
    print(y_list)
    print "===="


    re_fd.close()

    plt.scatter(x=x_list, y=y_list, label=label_list)
    # plt.grid(b=True, color='r', linestyle='-')
    plt.grid(b=True)

    for label, x, y in zip(label_list, x_list, y_list):
        if not label:
            continue
        plt.annotate(label, xy = (x, y), xytext = (-20, 20),
                     textcoords = 'offset points', ha = 'right',
                     va = 'bottom',bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5),
                     arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))

    plt.show()





    ''' average similarity of each grid '''

    ''' average tanimoto similarity of all feature vector '''
    # print distance.dist.cluster_similarity(matrix, {0: range(row)}, code_book)
    #
    #
    #
    # right_num = 0
    # same_cluster_num = 0
    # for k, v in bmus.items():
    #     for j in v:
    #         id = 0
    #         dis = 0
    #         for i in range(row):
    #             now = distance.dist.tanimoto_similarity(matrix[i], matrix[j])
    #
    #             if now < 1 and now  > dis:
    #                 dis = now
    #                 id = i
    #
    #         neighbors = []
    #         for c in range(som_x*som_y):
    #             if c in bmus.keys() and distance.bmu.is_neighbor(som_x, som_y, k, c, 1.5):
    #                 neighbors.extend(bmus[c])
    #
    #         if id not in neighbors:
    #             print j, id, k, neighbors
    #             print "best match feature is not neighbor"
    #         else:
    #             print "----------"
    #             right_num += 1
    #
    #         if id in bmus[k]:
    #             same_cluster_num += 1
    #
    # print row
    # print right_num
    # print same_cluster_num
    # #
    # #









