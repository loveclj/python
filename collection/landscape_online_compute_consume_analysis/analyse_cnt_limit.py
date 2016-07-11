#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: analyse_cnt_limit.py
@time: 7/1/16 10:26 AM
"""
import commands
if __name__ == '__main__':
    # data_dir = "../data/us_log/jobs"
    data_dir = "../data/jobs"

    cmd = "grep -r \"Cnt_limit\" " + data_dir
    status, output = commands.getstatusoutput(cmd)
    item_list = output.split("\n")

    solr_cnt_list = [100, 200, 500, 1000, 10000, 50000]
    cnt_freq = {}
    cnt_freq["other"] = 0
    for item in item_list:
        cnt = eval(item.split(':')[-1])
        if cnt not in solr_cnt_list:
            cnt_freq["other"] += 1
        else:
            if cnt in cnt_freq.keys():
                cnt_freq[cnt] += 1
            else:
                cnt_freq[cnt] = 1

    for k, v in cnt_freq.items():
        print k, v
