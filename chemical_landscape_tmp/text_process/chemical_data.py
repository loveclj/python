#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: chemical_data.py
@time: 7/7/16 10:52 AM
"""
import dynamodb
import dynamodb.scan
import dynamodb.extract_field
import time
import sys

def char2binary(c):
    b = bin(c)[2:]
    b = '0' * (8 - len(b)) + b
    return b


def str2binary(s, binary_begin=32, binary_end=-7):
    binary_list = map(char2binary, bytearray(s))
    binary = "".join(binary_list)[binary_begin: binary_end]
    return binary


def scan_chemical_data(table_name, fields, item_count, file_name):
    cid_fp = {}
    scanner = dynamodb.scan.Scanner(table_name=table_name, fields=fields)

    outfile_fp = open(file_name, 'w')

    n = 0
    while True:
        print 'scan'
        last_key, items = scanner.scan_once(limit=300)
        # print items
        print 'scan onece over'
        for item in items:
            try:
                cid = item['cid']['N']
                fp = item['fingerprint']['B']
                cid_fp[cid] = fp
                line = cid + ',' + str2binary(fp) + '\n'
                outfile_fp.write(line)
                n += 1
            except:
                print "no fingerprint", item['cid']['N']
                continue

        print n
        # time.sleep(1)

        if not last_key or n >= item_count:
            break

    outfile_fp.close()

if __name__ == '__main__':

    N = sys.maxint
    print N
    file_name = "chemical_data.text"
    cid_fp = scan_chemical_data('chemical', 'cid,fingerprint', N, file_name)

