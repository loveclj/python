#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site:
@file: tutorial.py.py
@time: 2/4/16 1:48 PM
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

data = [[1, 1], [0, 1], [2, 3], [3, 2]]
data = np.array(data)

label = [-1, 1, -1, 1]
label = np.array(label)

t = np.arange(-4, 4, 0.05)
learn_rate = 0.1

fig = plt.figure()

axes1 = fig.add_subplot(111)

data_trans = np.transpose(data)
axes1.scatter(data_trans[0], data_trans[1])

line, = axes1.plot(t, t * 0)

def update(p):
    w = p[0]
    b = p[1]

    w = w.reshape(1, -1)[0]
    print w
    if w[1] == 0:
        # if w[0] == 0:
        #     line, = axes1.plot(0, 0)
        if w[0] == 0:
            return line
        line.set_xdata([-b/w[0], -b/w[0]])
        line.set_ydata([1, 2])
    else:
        line.set_xdata(t)
        line.set_ydata((t*w[0]+b)/(-w[1]))
    return line,

def data_gen():
    feature_num = data.shape[0]
    dim = data.shape[1]

    w = np.zeros(dim).reshape(-1, 1)


    b = 0

    while True:
        error = 0
        for i in range(feature_num):
            out = np.dot(data[i], w) + b
            if 0.001 - out * label[i] >= 0:
                yield w, b
                w += data[i].reshape(-1, 1) * learn_rate * label[i]
                b += learn_rate * label[i]
                error += 1
                print error
        if error == 0:

            yield w, b
            break


ani = animation.FuncAnimation(fig, update, data_gen, interval=1000)

plt.show()

ws = data_gen()

attr = []
for w in ws:
    attr = w

w = attr[0]
b = attr[1]

for i in range(data.shape[0]):

    out = np.dot(data[i], w) + b
    print out, label[i]







