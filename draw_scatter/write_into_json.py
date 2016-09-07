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
    in_file_name = "bsom_sorted.text"
    out_file_name = "one_structure_per_grid.js"
    somx = 32
    somy = 32

    count = collections.defaultdict(int)
    list = []
    for line in open(in_file_name):
        label, grid = line.strip('\n').split(',')
        # print grid
        dic = {}
        dic["name"] = label
        dic["type"] = "scatter"

        grid = eval(grid)
        x = grid%somx + random.random()*0.3 + 0.5
        # x /= 10
        y = grid/somx + random.random()*0.3 + 0.5
        # y /= 10

        count[grid] += 1

        if count[grid] > 20:
            print grid
            continue


        data = [[x, y], ]
        dic["data"] = data
        list.append(dic)

    s = json.dumps(list, sort_keys=True, indent=4)
    # print s

    s = "var json_data = " + s

    fd = open(out_file_name, "w")
    fd.write(s)
