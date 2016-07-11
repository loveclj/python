#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: main.py
@time: 6/2/16 11:57 AM
"""


from __init__ import *
from char_covert import *


def is_uchar(uchar):
    # """判断一个unicode是否是汉字"""
    # if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
    #         return True
    """判断一个unicode是否是数字"""
    if uchar >= u'\u0030' and uchar<=u'\u0039':
            return True
    """判断一个unicode是否是英文字母"""
    if (uchar >= u'\u0041' and uchar<=u'\u005a') or (uchar >= u'\u0061' and uchar<=u'\u007a'):
            return True
    if uchar in ('-', ',', '\'', '.', '?', '!', '\"', ' ', ':'):
            return True
    return False


def process_fail_text_from_file(filename):

    string_mode = r'''[a-zA-Z0-9][a-zA-Z0-9 '.,"!?:‘’“”]+\/$'''
    pattern = re.compile(string_mode)
    count = 0

    with codecs.open(filename, mode="r", encoding="utf-8") as fd:
        while True:
            line = fd.readline().strip('\n')

            if not line:
                break

            illegal_char = False
            legal_char_list = []
            if not pattern.match(line):

                for c in line:

                    if not is_half_width_char(c):

                        c = convert_to_legal_char(c)

                        if not c:
                            illegal_char = True
                            break

                    legal_char_list.append(c)

            if illegal_char:
                print line
                continue

            count += 1
            # print convert_to_half_width_string(line)
        print count


if __name__ == '__main__':
    process_fail_text_from_file(fail_title_path)

