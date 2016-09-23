#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: main.py
@time: 9/13/16 11:06 AM
"""

import json
import csv

def load(filename, n, value_index=2, name_index=0):
    names = []
    matrix = []
    k = 0
    for line in open(filename):
        segs = line.strip('\n').split(',')
        # name = segs[name_index]
        name = ",".join(segs[0:2])
        v = segs[value_index]
        names.append(name)
        vec = []
        for i in v:
            vec.append(eval(i))

        matrix.append(vec)

        k += 1
        if k == n:
            break

    return names, matrix


def dist(vec1, vec2):
    s1 = sum(vec1)
    s2 = sum(vec2)
    com = 0
    for i in range(len(vec1)):
        if vec1[i] == vec2[i]:
            com += vec1[i]

    d = (1 - (float(com)/(s1 + s2 -com)))
    d = (float(com)/(s1 + s2 -com))
    # return int(d/0.01)

    return d

def buid_json(names, matrix):
    js = {}
    js["nodes"] = []
    for name in names:
        m = {"id": name, "group": 1}
        js["nodes"].append(m)

    js["links"] = []

    n = len(names)
    for i in range(n-1):
        # break
        for j in range(i+1, n):

            # try:
                d = dist(matrix[i], matrix[j])
                # if d < 0.8:
                #     continue

                # d = (d - 0.9) /0.05
                # d = d - 0.9
                m = {"source": names[i], "target": names[j], "value": d}
                js["links"].append(m)
            # except:
            #     print i, j

        #         if j > 5:
        #             break
        #
        # if i == 5:
        #     break


    return js




if __name__ == '__main__':

    names, matrix = load(filename='../data/name_formula_fingerprint_3k.text', n=1000)
    # print matrix
    # print len(matrix)
    # print len(names)
    # js = buid_json(names, matrix)
    #
    # str = json.dumps(js, indent=4)
    #
    # filename = "/home/lizhifeng/Downloads/forced_direct_graph/miserables.json"
    # # filename = "miserables.json"
    # fd = open(filename, 'w')
    # fd.write(str)
    # fd.close()


    f = open("distance.csv", 'wt')
    writer = csv.writer(f)
    # col_names = []
    n = 100
    for i in range(n):
        row = []
        for j in range(n):
            d = dist(matrix[i], matrix[j])
            row.append(d)

        writer.writerow(row)
    f.close()























