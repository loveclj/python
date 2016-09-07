#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: draw.py
@time: 8/23/16 3:27 PM
"""
import matplotlib.pyplot as plt


def load_coords(filename):
    x_list = []
    y_list = []
    label_list = []
    for line in open(filename):
        print line
        label, x, y = line.strip('\n').split(',')
        label_list.append(label)
        x_list.append(float(x))
        y_list.append(float(y))

    return label_list, x_list, y_list


def draw2d(x_list, y_list, label):

    plt.scatter(x=x_list, y=y_list)

    i = 0

    for label, x, y in zip(label, x_list, y_list):
        if i > 10:
            break

        label = label_list[i]
        i += 1
        # if label not in ['SCHEMBL14933', 'SCHEMBL30204']:
        #     continue
        plt.annotate(label, xy=(x, y), xytext=(-10, 10),
                     textcoords='offset points', ha='right',
                     va='bottom', bbox=dict(boxstyle='round,pad=0.3', fc='yellow', alpha=0.3),
                     arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))
    plt.show()

if __name__ == '__main__':
    # x_list, y_list = load_coords("/home/lizhifeng/git/glimmer/glimmer_cpu/glimmer/2D.text")
    # x_list, y_list = load_coords("/home/lizhifeng/cuda-workspace/MDS/2D.text")
    label_list, x_list, y_list = load_coords("/home/lizhifeng/cuda-workspace/MDS-2/2D.text")

    # for i in range(len(x_list)):
    #     label.append(str(i))

    draw2d(x_list, y_list, label_list)
