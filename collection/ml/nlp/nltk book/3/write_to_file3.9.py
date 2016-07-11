#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: write_to_file3.9.py.py
@time: 1/26/16 5:54 PM
"""

if __name__ == '__main__':

    output_fd = open("t", 'w')
    output_fd.write("hello")

    output_fd.close()