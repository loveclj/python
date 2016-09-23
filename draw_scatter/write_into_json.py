#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: write_into_json.py
@time: 8/26/16 4:09 PM
"""
import json
import random
import collections


if __name__ == '__main__':
    # in_file_name = "/home/lizhifeng/cuda-workspace/Binary_SOM/t"
    in_file_name = "/home/lizhifeng/cuda-workspace/MDS-2/2D.text"

    out_file_name = "one_structure_per_grid.js"
    out_file_name = "1000_MDS.js"
    out_file_name = "/home/lizhifeng/Downloads/mds_display_1k/2D.js"
    out_file_name = "/home/lizhifeng/Downloads/mds_display_1k_no_overlap/2D.js"

    count = collections.defaultdict(int)
    list = []

    n = 0
    for line in open(in_file_name):
        label, x, y = line.strip('\n').split(',')
        # print grid
        dic = {}
        dic["name"] = label
        dic["type"] = "scatter"

        # x = eval(x) + random.random()*0.3 + 0.5
        # # x /= 10
        # y = eval(y) + random.random()*0.3 + 0.5
        # # y /= 10
        #
        # coord = str(x) + "," + str(y)
        # count[coord] += 1
        #
        # if count[coord] > 20:
        #     print coord
        #     continue

        x = int(eval(x) / 0.01) + 0.5
        y = int(eval(y) / 0.01) + 0.5
        data = [[x, y], ]
        dic["data"] = data
        list.append(dic)

        # n += 1
        # if n == 500:
        #     break

    s = json.dumps(list, sort_keys=True, indent=4)
    # print s

    s = "var json_data = " + s

    fd = open(out_file_name, "w")
    fd.write(s)
