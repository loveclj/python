#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: bmu.py
@time: 7/14/16 4:09 PM
"""

import dist
import numpy as np
from collections import defaultdict


def find_bmu(code_book, data_matrix):

    grid_num = code_book.shape[0]
    data_count = data_matrix.shape[0]

    print data_count, "data count"

    bmu_grid_item_id = defaultdict(list)

    for i in range(data_count):
        max_similarity = 0
        max_grid_id = 0
        for j in range(grid_num):
            similarity = dist.tanimoto_similarity(data_matrix[i], code_book[j])
            # if i == 0:
            #     print j, similarity
            if max_similarity < similarity:
                max_similarity = similarity
                max_grid_id = j

        bmu_grid_item_id[max_grid_id].append(i)

    return bmu_grid_item_id


def is_neighbor(som_x, som_y, grid_a_id, grid_b_id, radius):

    a_x = grid_a_id % som_x
    a_y = grid_a_id / som_x

    b_x = grid_b_id % som_x
    b_y = grid_b_id / som_x

    if pow(abs(b_x - a_x), 2) + pow(abs(b_y - a_y), 2) <= radius * radius:
        return True
    else:
        return False


def update_code_book(som_x, som_y, bums, matrix, code_book, radius, weight):

    dimenssion = matrix.shape[1]
    som_grid_count = code_book.shape[0]

    for grid_id in range(som_grid_count):

        ''' find all neigbors of grid_id '''
        neighbors = []
        for c in range(som_grid_count):
            if is_neighbor(som_x, som_y, grid_id, c, radius=radius):
                neighbors.append(c)

        ''' get all data vector best matching grids collection neighbors '''
        neighbors_bmus = []
        for c in neighbors:
            if c in bums.keys():
                neighbors_bmus.extend(bums[c])

        item_count = 0
        sum_vec = [0] * dimenssion
        for i in neighbors_bmus:
            vec = matrix[i]
            item_count += 1
            for j in range(dimenssion):
                sum_vec[j] += vec[j]

        '''  minimize loss function '''
        for j in range(dimenssion):

            if sum_vec[j] * 2 >= item_count * weight[j]:
                code_book[grid_id][j] = weight[j]
            else:
                code_book[grid_id][j] = 0

    return code_book


if __name__ == '__main__':
    print find_bmu([[2], [2]], [])
