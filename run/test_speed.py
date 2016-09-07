#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: test_speed.py
@time: 9/5/16 5:48 PM
"""
import commands


if __name__ == '__main__':

    path = "/home/lizhifeng/cuda-workspace/Binary_SOM"
    count_list = [100, 500, 1000, 2000, 5000, 10000, 20000, 50000]
    # count_list = [100, 500, 1000, 2000]
    count_list = [50000]
    count_per_grid_list = [1, 2, 5, 10, 20, 50, 100]
    count_per_grid_list = [50, 100]

    for count in count_list:
        for count_per_grid in count_per_grid_list:
            grid_count = count / count_per_grid
            if grid_count < 20:
                continue

            if grid_count > 2000:
                continue

            cmd = "cd " + path + ";"
            cmd += "./Release/Binary_SOM  name_formula_fingerprint_150k.text weight.txt %d %d" %(count, count_per_grid)
            status, output = commands.getstatusoutput(cmd)

            try:
                if status:
                    print " error excute ", cmd

                train_time = output.split(' ')[-2]
                print count, count_per_grid, train_time
            except:
                pass



