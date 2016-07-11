#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: test_networkx.py
@time: 6/28/16 6:05 PM
"""

import networkx as nx
import matplotlib.pyplot as plt

def draw_a_dot(n):
    G = nx.Graph()
    G.add_node(n)
    G.add_node(n+1)
    G.add_node("x")
    G.add_node("y")
    nx.draw(G)
    plt.show()

if __name__ == '__main__':
    draw_a_dot(2)
