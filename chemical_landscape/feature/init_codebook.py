#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: init_codebook.py
@time: 7/14/16 2:41 PM
"""


import random
import numpy as np


def random_bin_init_codebook(som_x, som_y, dimenssion, threshold=0.5):
    code_book = []
    random.seed(1)
    for i in range(som_x * som_y):
        vec = []
        for j in range(dimenssion):
            if random.random() > threshold:
                vec.append(1)
            else:
                vec.append(0)

        code_book.append(vec)

    return np.array(code_book)


if __name__ == '__main__':
    print random_bin_init_codebook(2, 1, 3)