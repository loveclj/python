#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: get_feature_vecotr.py
@time: 7/25/16 5:21 PM
"""

import boto3
import dynamodb.batch_get as batch_get
import base64

def char2binary(c):
    b = bin(c)[2:]
    b = '0' * (8 - len(b)) + b
    return b


def str2binary(s, binary_begin=32, binary_end=-7):
    binary_list = map(char2binary, bytearray(s))
    binary = "".join(binary_list)[binary_begin: binary_end]
    return binary



if __name__ == '__main__':

    '''　ch4 '''
    a = "AAADcYBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAACAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=="
    ''' ch3ch3 '''
    b = "AAADcYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=="
    ''' ch3choh '''
    c = "AAADcYBAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGgAACAAAAACggAICAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=="
    ''' ch3ch2ch3 '''
    d = "AAADccBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAACACAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=="
    ''' ch3ch2ch2oh '''
    e = "AAADccBAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGgAACAAACACggAICAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAEAAAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=="
    ''' hcooh'''
    f = "AAADcQAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEgAACAAAAAAAAAMACAAAAgAIAAAAiAAAAAAAAAAAAAAAAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=="


    a = base64.decodestring(a)
    a_f = str2binary(a)


    b = base64.decodestring(b)
    b_f = str2binary(b)



    c = base64.decodestring(c)
    c_f = str2binary(c)

    d = base64.decodestring(d)
    d_f = str2binary(d)

    e = base64.decodestring(e)
    e_f = str2binary(e)

    f = base64.decodestring(f)
    f_f = str2binary(f)

    fd = open("feature.text", 'w')
    line = "1" + "," + a_f + "\n"
    fd.write(line)

    line = "2" + "," + b_f + "\n"
    fd.write(line)

    line = "3" + "," + c_f + "\n"
    fd.write(line)

    line = "4" + "," + d_f + "\n"
    fd.write(line)

    line = "5" + "," + e_f + "\n"
    fd.write(line)

    line = "6" + "," + f_f + "\n"
    fd.write(line)

    fd.close()

    print b_f
    print e_f





    # client = batch_get.BatchGet(table_name='chemical', fields=['cid', 'fingerprint'])
    # r = client.batch_get_once(key_list=[{'cid': {'N': '1'}}])
    # print r
    #
    #
    # cid_file_name = '5h3t.text'
    # fingerprint_file_name = '5h3t_fingerprint.text'
    #
    # with open(cid_file_name, 'r') as fd, open(fingerprint_file_name, 'w') as out_fd:
    #     while True:
    #         line = fd.readline()
    #         if not line:
    #             break
    #
    #         cid = line.strip('\n')
    #
    #         r = client.batch_get_once(key_list=[{'cid': {'N': cid}}])
    #         try:
    #
    #             binary = r['Responses']['chemical'][0]['fingerprint']['B']
    #             fingerprint = str2binary(binary)
    #             line = cid + ',' + fingerprint + '\n'
    #             out_fd.write(line)
    #
    #
    #         except:
    #             continue