#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: convert.py
@time: 8/17/16 10:05 AM
"""

if __name__ == '__main__':
    file_name = "chemical_data_10k"
    out_file_name = "out.text"
    fd = open(out_file_name, 'w')
    for line in open(file_name):
        id, fp = line.strip('\n').split(',')

        line = id + "," + id + "," + fp + '\n'
        fd.write(line)

    fd.close()
