#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: convert_sparse_to_matrix.py
@time: 7/14/16 1:49 PM
"""

def convert_sparse_to_matrix(infile_name, outfile_name):
    with open(infile_name, "r") as in_fp, open(outfile_name, "w") as out_fp:
        while True:
            line = in_fp.readline()
            if not line:
                break

            l = line.strip('\n').split(',')
            out_line = str(l[0]) + ','
            index = 0
            for e in l[1:]:
                e = int(e)

                while index < e:
                    out_line += str(0)
                    index += 1

                out_line += str(1)
                index += 1

            while index < 881:
                out_line += str(0)
                index += 1

            out_line += '\n'
            out_fp.write(out_line)


if __name__ == '__main__':
    convert_sparse_to_matrix('./chemical_sparse_data.text', "./chemical_data.text")