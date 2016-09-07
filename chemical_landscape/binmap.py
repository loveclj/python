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
from collections import defaultdict


def load_weight_from_file(file_name):
    weight = [0] * dimenssion

    for line in open(file_name):

            id, p = line.split(':')[:2]
            id = int(id)
            p = float(p)
            weight[id] = p

    return np.array(weight)


def load_codebook(somx, somy, dimenssion, filename, weight):
    code_book = []

    v_list = []
    for line in open(filename):
        # f =
        v_list.append(eval(line.strip('\n')))

    for i in range(som_x*som_y):
        vec = []
        for j in range(dimenssion):

            if v_list[i*dimenssion+j] > 0:
                vec.append(weight[j])
            else:
                vec.append(0)

        code_book.append(vec)

    return np.array(code_book)


if __name__ == '__main__':
    row = 1000
    som_x = 10
    som_y = 10
    dimenssion = 881

    # feature_file_name = "chemical_data_10k"
    feature_file_name = "formula_figerprint.text"
    feature_file_name = "formula_figerprint_ali_data_set2.text"
    feature_file_name = "formula_figerprint_ali_suger_data.text"
    feature_file_name = "name_formula_fingerprint_3k.text"
    cid, matrix = ft.get_feature_matrix_from_file(feature_file_name, row)
    weight = load_weight_from_file('id_info.text')

    code_book = load_codebook(som_x, som_y, dimenssion, "codebook.text", weight)

    matrix = matrix * weight

    total_epoch = som_x
    # total_epoch = 0
    first_train = True
    result_pre = None
    for i in range(total_epoch):

      max_train_times_per_epoch = 0
      # radius = int(som_x/2 - i)
      radius = som_x/2 - i * 0.3

      if radius < 0:
          break


      while True:
        print "radius is", radius
        max_train_times_per_epoch += 1
        if max_train_times_per_epoch >= 100:
            break

        bmus = distance.bmu.find_bmu(code_book, matrix)

        ''' update code book '''
        code_book = distance.bmu.update_code_book(som_x, som_y, bmus, matrix, code_book, radius, weight)

        for r in range(som_y*som_x):
            for d in range(dimenssion):
                print code_book[r][d]

        # result_now = distance.dist.cluster_similarity(matrix, bmus, code_book)
        #
        # if result_now == result_pre:
        #     print "***** stable ****"
        #     break
        # else:
        #     result_pre = result_now
        #     print "******** not stable ********"

        break
      break

    bmus = distance.bmu.find_bmu(code_book, matrix)

    for k, v in bmus.items():
            print k, v


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

            # print i, cid[i]

            line = str(i) + "," + cid[i] + "\n"
            re_fd.write(line)

        re_fd.write('======================')


    re_fd.close()





