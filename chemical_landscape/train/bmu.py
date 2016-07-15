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


def four_neighbor(som_x, som_y, n):
    x = n % som_x
    y = n / som_x

    neighbor = []
    if x - 1 >= 0:
        neighbor.append(n - 1)

    if x + 1 < som_x:
        neighbor.append(n + 1)

    if y - 1 >= 0:
        neighbor.append(som_x*(y-1) + x)

    if y + 1 < som_y:
        neighbor.append(som_x*(y+1) + x)

    return neighbor


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


def update_code_book(som_x, som_y, bums, matrix, code_book):

    dimession = len(matrix[0])

    for i in range(len(code_book)):
        # if i not in bums.keys():
        #     continue

        sum_vec = [0] * dimession
        item_num = 0
        neighbor = four_neighbor(som_x, som_y, i)
        neighbor.append(i)

        cur_bmus = []
        for c in neighbor:
            if c in bums.keys():
                cur_bmus.extend(bums[c])

        # cur_bmus.extend(bums[i])

        for k in cur_bmus:
            vec = matrix[k]
            item_num += 1
            for j in range(dimession):
                sum_vec[j] += vec[j]

        for j in range(dimession):
            if sum_vec[j] * 2 >= item_num:
                code_book[i][j] = 1
            else:
                code_book[i][j] = 0

    return code_book


def update_code_book2(som_x, som_y, bums, matrix, code_book):

    dimession = len(matrix[0])

    for i in range(len(code_book)):
        # if i not in bums.keys():
        #     continue

        sum_vec = [0] * dimession
        item_num = 0
        neighbor = four_neighbor(som_x, som_y, i)
        neighbor.append(i)

        if i in bums.keys():
            cur_bmus = bums[i]
        else:
            continue
        # cur_bmus.extend(bums[i])

        for k in cur_bmus:
            vec = matrix[k]
            item_num += 1
            for j in range(dimession):
                sum_vec[j] += vec[j]

        for j in range(dimession):
            if sum_vec[j] * 2 >= item_num:
                code_book[i][j] = 1
            else:
                code_book[i][j] = 0

    return code_book

if __name__ == '__main__':
    print find_bmu([[2], [2]], [])
