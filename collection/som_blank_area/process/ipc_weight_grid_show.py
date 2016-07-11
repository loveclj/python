#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site:
@file: ipc_weight_grid_show.py
@time: 4/20/16 2:07 PM
"""
import matplotlib.pyplot as plt
import matplotlib
from mpl_toolkits.axes_grid1 import ImageGrid
import numpy as np
from mpl_toolkits.axes_grid.grid_helper_curvelinear import  GridHelperCurveLinear
from mpl_toolkits.axes_grid.axislines import Subplot
import mpl_toolkits.axes_grid.angle_helper as angle_helper

import load_text


def show_grid_gray(weight, height, data):
    a = np.arange(0, height+1, 1)
    b = np.arange(0, weight+1, 1)
    A, B = np.meshgrid(a, b)
    data.shape = weight, height

    print data

    plt.pcolor(A, B, data)
    plt.show()

def show_gray_matrix(matrix):
    camp = matplotlib.cm.gray_r
    norm = matplotlib.colors.Normalize(vmin=0)
    plt.show(matrix, camp=camp)

def show_grid(weight, height):
    for idx in range(weight):
        plt.hlines(idx, 0 , height)
        plt.vlines(idx, 0, height)

    plt.axes().set_aspect('equal')
    plt.show()

def show_ipc_weight(weight, height, array):

        array.shape = weight, height
        fig = plt.figure(1, (4., 4.))
        grid = ImageGrid(fig, 111, nrows_ncols=(2, 2), axes_pad=0.1)

        for i in range(4):
            grid[i].imshow(array)

        plt.show()


def get_col_from_matrix(matrix, index):
    col = []
    for row, vector in matrix.items():
        col.append(vector[index])
    return col


if __name__ == '__main__':

    matrix = load_text.load_matrix("../text/codebook.text")
    print matrix
    col = get_col_from_matrix(matrix, 37)

    array = np.array(col)
    # show_ipc_weight(5, 7, array)
    array.shape = 5, 7
    # show_gray_matrix(array)

    # show_grid(5, 7)
    show_grid_gray(5, 7, array)


