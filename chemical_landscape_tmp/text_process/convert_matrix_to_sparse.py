#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: convert_matrix_to_sparse.py
@time: 7/12/16 2:25 PM
"""

def  convert(infilename, outfilename):
    infp = open(infilename, 'r')
    outfp = open(outfilename, 'w')

    while True:
        line = infp.readline()
        if not line:
            break

        id, fingerprint = line.strip('\n').split(',')
        print id, fingerprint

        out_line = id

        i = 0
        for c in fingerprint:
            if c == '1':
                out_line += ',' + str(i)

            i += 1

        out_line += '\n'

        outfp.write(out_line)

    infp.close()
    outfp.close()


if __name__ == '__main__':
    convert('./chemical_data.text', 'chemical_sparse_data2.text')