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


def load_weight_from_file(file_name, dimension):
    weight = [0] * dimension

    for line in open(file_name):

            id, p = line.split(':')[:2]
            id = int(id)
            p = float(p)
            weight[id] = p

    return np.array(weight)


def load_data(file_name):
    smiles = []
    clusters = []
    matrix = []

    i = 0
    for line in open(file_name):
        if i == 13:
            continue

        i += 1

        s, c, m = line.strip('\n').split(',')

        smiles.append(s)
        clusters.append(c)

        vec = []
        for e in m:
            vec.append(int(e))

        matrix.append(vec)

    return smiles, clusters, matrix


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


def mds(matrix, rate=0.01):
    u_matrix = distance_matrix(matrix, tanimoto_distance)
    row = len(matrix)
    loc = [[random.random(), random.random()] for i in range(row)]
    fake_distance = [[0.0 for i in range(row)] for j in range(row)]

    last_error = None

    for m in range(1000):
        for i in range(row):
            for j in range(row):
                fake_distance[i][j] = math.sqrt(sum([pow(loc[i][x] - loc[j][x], 2) for x in range(len(loc[i]))]))

        grad = [[0.0, 0.0] for i in range(row)]

        total_error = 0
        for i in range(row):
            for j in range(row):
                if i == j:
                    continue

                error_term = (fake_distance[i][j] - u_matrix[i][j])/u_matrix[i][j]

                grad[i][0] += (loc[i][0] - loc[j][0])/fake_distance[i][j] * error_term
                grad[i][1] += (loc[i][1] - loc[j][1])/fake_distance[i][j] * error_term

                total_error += abs(error_term)

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
        plt.annotate(label, xy = (x, y), xytext = (-20, 20),
                     textcoords = 'offset points', ha = 'right',
                     va = 'bottom',bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5),
                     arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))
    plt.show()


if __name__ == '__main__':
    smiles, clusters, matrix = load_data('data/smiles_cluster_fingerprint.text')
    print smiles

    matrix = np.array(matrix)

    dimension = 881
    weight = load_weight_from_file('./data/id_info.text', dimension)
    matrix = matrix * dimension

    loc = mds(matrix, 0.02)

    draw2d(loc, clusters)