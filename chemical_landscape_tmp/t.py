#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: t.py.py
@time: 7/29/16 4:38 PM
"""

if __name__ == '__main__':

    i = 0
    out_file = "id_cluster_smiles.text"
    fd = open(out_file, 'w')
    for line in open("formula_figerprint_ali_data_set.text"):
        smiles, cluster = line.strip('\n').split(',')

        line = str(i) + ","  + " "*(4 - len(str(i))) + cluster + "," + " "*8 + smiles + '\n'
        print line
        i += 1
        fd.write(line)

    fd.close()