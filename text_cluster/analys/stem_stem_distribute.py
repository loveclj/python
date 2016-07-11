#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: stem_stem_distribute.py
@time: 6/28/16 5:03 PM
"""

import matplotlib.pyplot as plt
import networkx as nx
import fileIO


def filter_map_by_value(dict, threshold):
    dict_filtered = {}
    for k, v in dict.items():
        if eval(v) > threshold:
            dict_filtered[k] = v

    return dict_filtered


def filter_map_by_stopwords(dict, stopwords):
    dict_filtered = {}
    for k, v in dict.items():
        w1, w2 = k.split(',')
        if w1 in stopwords or w2 in stopwords:
            continue

        dict_filtered[k] = v

    return dict_filtered


def draw_graph(node_node_value_list):
    G = nx.Graph()

    i = 0
    nodes = []
    for node_node_value in node_node_value_list:

        if node_node_value[0] not in nodes:
            G.add_node(node_node_value[0])
        if node_node_value[1] not in nodes:
            G.add_node(node_node_value[1])

        G.add_edge(node_node_value[0], node_node_value[1], weight=int(node_node_value[2]))

    nx.draw_circular(G, node_size=80, with_labels=True)
    plt.show()


def compare_weight(a, b, n=2):
    return a[n] - b[n]


if __name__ == '__main__':

    # stem_stem_file = "../result/stem_stem_freq.text"
    # stem_stem_file = "filtered_result"

    # stopwords = fileIO.load.load_list_from_file("../data/stopwords.text")
    #
    # stem_stem_freq = fileIO.dumps.load_map_from_file(stem_stem_file)
    # dict_filtered = filter_map_by_stopwords(stem_stem_freq, stopwords)
    # dict_filtered = filter_map_by_value(dict_filtered, 1000)
    #
    # fileIO.dumps.dump_map_to_file(dic=dict_filtered, mode='w', filename="./filtered_result.text")

    # fileIO.dumps.print_map(stem_stem_freq)

    stem2stem_freq_list = fileIO.load.load_list_list_from_file("t")

    l = set()
    w = "region"
    for k in stem2stem_freq_list:
        if k[0] == w or k[1] == w:
            l.add((k[0], k[1], int(k[2])))
            # print k

    l = sorted(l, cmp=compare_weight, reverse=True)[:10]
    l = set(l)
    next = [x[1] for x in l]

    for w in next:
        print w
        tmp = set()
        for k in stem2stem_freq_list:


            if k[0] == w or k[1] == w:
                tmp.add((k[0], k[1], int(k[2])))

        tmp = sorted(tmp, cmp=compare_weight, reverse=True)[:10]
        # print tmp
        l.update(tmp)


    l = sorted(l, cmp=compare_weight, reverse=True)[:100]
    draw_graph(l)
    # draw_graph(stem2stem_freq_list)

