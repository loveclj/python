#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: bmu.py
@time: 7/14/16 4:09 PM
"""

import sys
sys.path.append("..")
import distance.tanimoto as tanimoto


def find_bmu(code_book, feature_matrix):
    grid_num = len(code_book)
    bmus = {}

    for i in range(len(feature_matrix)):
        max_similarity = 0
        max_grid_id = 0
        for j in range(grid_num):
            similarity = tanimoto.bin_tanimoto_similarity(feature_matrix[i], code_book[j])
            if max_similarity < similarity:
                max_similarity = similarity
                max_grid_id = j

        if max_grid_id not in bmus.keys():
            bmus[max_grid_id] = [i]
        else:
            bmus[max_grid_id].append(i)

    return bmus


def is_neighbor(som_x, som_y, center, n, radius):
    center_x = center % som_x
    center_y = center / som_x

    n_x = n % som_x
    n_y = n / som_y

    if abs(n_x - center_x) <= radius and abs(n_y - center_y) <= radius:
        return True
    else:
        return False


def update_code_book(som_x, som_y, bums, matrix, code_book, radius):

    dimession = len(matrix[0])

    for i in range(len(code_book)):

        sum_vec = [0] * dimession
        item_num = 0

        neighbor = [i]

        for c in range(len(code_book)):
            if is_neighbor(som_x, som_y, center=i, n=c, radius=radius):
                neighbor.append(c)

        cur_bmus = []
        for c in neighbor:
            if c in bums.keys():
                cur_bmus.extend(bums[c])

        for k in cur_bmus:
            vec = matrix[k]
            item_num += 1
            for j in range(dimession):
                sum_vec[j] += vec[j]

        '''  minimize loss function '''
        for j in range(dimession):
            if sum_vec[j] * 2 >= item_num:
                code_book[i][j] = 1
            else:
                code_book[i][j] = 0

    return code_book


if __name__ == '__main__':
    print find_bmu([[2], [2]], [])
