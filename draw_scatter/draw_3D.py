#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: draw_3D.py
@time: 8/29/16 10:58 AM
"""

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import random
import math


def fun(x, y):
  return x**2 + y


def load_coords(filename):
    coords = []
    for line in open(filename):
        label, x, y = line.strip('\n').split(',')
        coords.append((float(x), float(y)))

    return coords


center_coords = load_coords("2D.text")


def gaussion_mountain(x, y):
    h = 0
    for cx, cy in center_coords:
        h += 1/(2 * math.pi) * math.exp(-500*(pow(x-cx, 2) + pow(y-cy, 2)))

    return h


def draw_3D(fun):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x = y = np.arange(0, 1.0, 0.001)
    X, Y = np.meshgrid(x, y)
    zs = np.array([fun(x,y) for x,y in zip(np.ravel(X), np.ravel(Y))])
    Z = zs.reshape(X.shape)

    ax.plot_surface(X, Y, Z)

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    plt.show()


if __name__ == "__main__":
    print center_coords

    draw_3D(gaussion_mountain)