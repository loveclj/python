#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: matrix.py
@time: 8/5/16 3:49 PM
"""

import random
import math
import matplotlib.pyplot as plt
import numpy as np
import sys


def load_weight_from_file(file_name, dimension):
    weight = np.zeros(dimension)

    for line in open(file_name):

            id, p = line.split(':')[:2]
            id = int(id)
            p = float(p)
            weight[id] = p

    return weight


def load_data(file_name):
    smiles = []
    clusters = []
    matrix = []

    feature_set = set()

    for line in open(file_name):

        s, c, m = line.strip('\n').split(',')

        # if m in feature_set:
        #     print s
        #     continue
        # else:
        #     feature_set.add(m)

        smiles.append(s)
        clusters.append(c)

        vec = []
        for e in m:
            vec.append(int(e))

        matrix.append(vec)

    return smiles, clusters, matrix


def load_data_with_name(file_name):
    smiles = []
    names = []
    matrix = []

    feature_set = set()

    for line in open(file_name):

        n, s, m = line.strip('\n').split(',')

        if m in feature_set:
            print s
            continue
        else:
            feature_set.add(m)

        smiles.append(s)
        names.append(n)

        vec = []
        for e in m:
            vec.append(int(e))

        matrix.append(vec)

    return names, smiles, matrix

def tanimoto_distance(vec1, vec2):
    sum1 = sum(vec1)
    sum2 = sum(vec2)

    sum_comm = 0
    for i in range(len(vec1)):
        if vec1[i] == vec2[i]:
            sum_comm += vec1[i]

    return 1 - float(sum_comm) / (sum1 + sum2 - sum_comm)


def distance_matrix(matrix, func):
    u_matrix = []
    row = len(matrix)
    for i in range(row):
        vec = []
        for j in range(row):
            dis = func(matrix[i], matrix[j])
            vec.append(dis)
        u_matrix.append(vec)

    return u_matrix


def mds(matrix, total_epoch=1000, rate=0.01):
    u_matrix = distance_matrix(matrix, tanimoto_distance)
    row = len(matrix)
    random.seed(1)
    loc = [[random.random(), random.random()] for i in range(row)]
    fake_distance = [[0.0 for i in range(row)] for j in range(row)]

    last_error = None

    for m in range(total_epoch):
        for i in range(row):
            for j in range(row):
                 fake_distance[i][j] = math.sqrt(sum([pow(loc[i][x] - loc[j][x], 2) for x in range(len(loc[i]))]))

        scale = 0
        abs_error = 0
        for i in range(row):
            for j in range(i, row):
                scale += fake_distance[i][j] ** 2
                abs_error += (fake_distance[i][j] - u_matrix[i][j]) ** 2

        grad = [[0.0, 0.0] for i in range(row)]

        total_error = 0
        for i in range(row):
            for j in range(row):
                if i == j:
                    continue

                fake_distance[i][j] = math.sqrt(sum([pow(loc[i][x] - loc[j][x], 2) for x in range(len(loc[i]))]))

                # error_term = 0
                # if fake_distance[i][j] > u_matrix[i][j]:
                #     error_term = 1.0/(u_matrix[i][j])
                #     # error_term = 1.0
                # else:
                #     error_term = -1.0/(u_matrix[i][j])
                #     # error_term = -1.0

                # error_term = (fake_distance[i][j] - u_matrix[i][j])/(u_matrix[i][j] ** 2)


                error_term = (fake_distance[i][j] - u_matrix[i][j]) / fake_distance[i][j] * scale - abs_error

                grad[i][0] += (loc[i][0] - loc[j][0]) * error_term
                grad[i][1] += (loc[i][1] - loc[j][1]) * error_term

                total_error += abs(error_term)

            # loc[i][0] -= rate*grad[i][0]
            # loc[i][1] -= rate*grad[i][1]

            # if i == 2:
            #     print grad[2]

        for k in range(row):
                loc[k][0] -= rate*grad[k][0]/(scale ** 2)
                loc[k][1] -= rate*grad[k][1]/(scale ** 2)

        print "total_error", total_error

    return loc


def mds_origin(matrix, total_epoch=1000, rate=0.01):
    u_matrix = distance_matrix(matrix, tanimoto_distance)
    row = len(matrix)
    random.seed(1)
    loc = [[random.random(), random.random()] for i in range(row)]
    fake_distance = [[0.0 for i in range(row)] for j in range(row)]

    last_error = None

    for m in range(total_epoch):
        for i in range(row):
            for j in range(row):
                 fake_distance[i][j] = math.sqrt(sum([pow(loc[i][x] - loc[j][x], 2) for x in range(len(loc[i]))]))

        grad = [[0.0, 0.0] for i in range(row)]

        total_error = 0
        for i in range(row):
            for j in range(row):
                if i == j:
                    continue


                # error_term = 0
                # if fake_distance[i][j] > u_matrix[i][j]:
                #     error_term = 1.0/(u_matrix[i][j])
                #     # error_term = 1.0
                # else:
                #     error_term = -1.0/(u_matrix[i][j])
                #     # error_term = -1.0

                error_term = (fake_distance[i][j] - u_matrix[i][j])#/(u_matrix[i][j])

                grad[i][0] += (loc[i][0] - loc[j][0])/fake_distance[i][j] * error_term
                grad[i][1] += (loc[i][1] - loc[j][1])/fake_distance[i][j] * error_term

                total_error += abs(error_term)

            # loc[i][0] -= rate*grad[i][0]
            # loc[i][1] -= rate*grad[i][1]

        for k in range(row):
                loc[k][0] -= rate*grad[k][0]
                loc[k][1] -= rate*grad[k][1]

        print "total_error", total_error

    return loc


def draw2d(data, label):
    x_list = [data[x][0] for x in range(len(data))]
    y_list = [data[x][1] for x in range(len(data))]
    plt.scatter(x=x_list, y=y_list)

    for label, x, y in zip(label, x_list, y_list):
        plt.annotate(label, xy = (x, y), xytext = (-10, 10),
                     textcoords = 'offset points', ha = 'right',
                     va = 'bottom',bbox = dict(boxstyle = 'round,pad=0.3', fc = 'yellow', alpha = 0.3),
                     arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))
    plt.show()


def hierarchicalCluster(distance_mat):
    item_count = len(distance_mat)
    steps = []
    cluster_record = [[i] for i in range(item_count)]
    mat = distance_mat
    print mat
    for i in range(item_count -1):
        print "cluster num", len(distance_mat) - 1 - i

        min_distance = sys.float_info.max
        pair = (0, 0)
        for j in range(len(mat)):
            for k in range(j):
                if mat[j][k] < min_distance and mat[j][k] > 0:
                    pair = (k, j)
                    min_distance = mat[j][k]

        cluster_record[pair[0]].extend(cluster_record[pair[1]])

        steps.append(pair)

        merged_id = cluster_record[pair[1]][0]

        for m in range(len(mat)):
            mat[m][merged_id] = -1 * (mat[m][merged_id])#sys.float_info.max
            mat[merged_id][m] = -1 * (mat[m][merged_id])#sys.float_info.max

        cluster_record[pair[1]] = []

        min = sys.float_info.max
        '''update matrix distance '''
        for m in range(len(mat)):
            if not cluster_record[m]:
                continue

            dist = 0
            n = 0
            for x in cluster_record[m]:
                for y in cluster_record[pair[0]]:
                    # dist += abs(mat[x][y])
                    # n += 1
                    if 0 < mat[x][y] < min:
                        min = mat[x][y]

            mat[m][cluster_record[pair[0]][0]] = min #dist / n
            mat[cluster_record[pair[0]][0]][m] = min #dist / n
        print steps
        print cluster_record

    # print steps


if __name__ == '__main__':
    # smiles, clusters, matrix = load_data('data/smiles_cluster_fingerprint.text')
    names, smiles, matrix = load_data_with_name('data/test_data_MDS_64_SMILES_fingerprint.text')

    matrix = np.array(matrix)

    dimension = 881
    weight = load_weight_from_file('./data/id_info.text', dimension)
    matrix = matrix * weight

    dis_mat = distance_matrix(matrix, tanimoto_distance)

        # print
    # # hierarchicalCluster(dis_mat)
    #
    loc = mds_origin(matrix, 10000, 0.001)

    label = []
    i = 0
    for c in names:
    # for c in clusters:
        label.append(str(i) ) #+ ',' + c)
        i += 1

    # fd = open("cluster_reslut.text", 'w')
    # for i in range(len(names)):
    #     line = str(i) + " " *(5 - len(str(i))) + names[i] + " " * (20 - len(names[i])) + smiles[i] + '\n'
    #     fd.write(line)
    # fd.close()


    draw2d(loc, label)