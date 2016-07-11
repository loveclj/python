#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: ipc2upc.py
@time: 4/14/16 2:55 PM
"""


def load_ipc2upc(filename):
    ipc2upc ={}
    with open(filename, "r") as fd:
        lines = fd.readlines()

        line_count = len(lines)
        for i in range(line_count/2):
            ipc = lines[2*i].strip('\n')
            upcs = lines[2*i+1].strip('\n').split(',')

            ipc2upc[ipc] = []
            for upc in upcs:
                ipc2upc[ipc].append(eval(upc))

    return ipc2upc

if __name__ == '__main__':

    print load_ipc2upc("../text/ipc2upc.text")