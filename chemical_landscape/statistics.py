#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: statistics.py
@time: 7/7/16 12:46 PM
"""
def feature_df(filename, dimenssion):
    df = [0] * dimenssion
    fp = open(filename, 'r')

    line_num = 0
    while True:
        line = fp.readline()

        if not line:
            break

        line_num += 1

        if line_num % 10000 == 0:
            print line_num

        cid, fingerprint = line.strip('\n').split(',')
        for i in range(dimenssion):
            df[i] += int(fingerprint[i])

    fp.close()

    return df, line_num

# def


if __name__ == '__main__':

    dimension = 881
    fingerprint_df, fp_count = feature_df('chemical_data.text', dimension)
    fp = open('df.text', 'w')
    print fingerprint_df
    print fp_count

    n = 0
    for i in range(dimension):
        line = str(i) + ',' + str(fingerprint_df[i]) + '\n'
        fp.write(line)
        n += fingerprint_df[i]

    print n/dimension
    fp.close()
