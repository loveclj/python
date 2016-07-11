#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: build_dict.py
@time: 5/16/16 10:20 AM
"""

import codecs
import commands

def list_dir(dir):
    cmd = "ls " + dir
    status, output = commands.getstatusoutput(cmd)
    file_list = output.split()

    for i in range(len(file_list)):
        file_list[i] = dir + "/" + file_list[i]

    return file_list


def load_file(filename, en_cn_dict, cn_count_limit):

    with codecs.open(filename, "r", "utf-8") as fd:

        lines = fd.readlines()
        line_count = len(lines)

        for i in range(line_count/2):
            en_words_list = lines[2*i].strip('\n')[:-2].split(";")
            cn_words_list = lines[2*i+1].strip('\n')[:-2].split(";")
            # print en_words_list
            # print cn_words_list

            if len(en_words_list) != len(cn_words_list):
                # print lines[2*i+1]
                err_msg = "[ERROR] number of cn and en words are not equal"
                info_msg = "[INFO] filename: " + filename + "\n"
                info_msg += "[INFO] line: " + str(2*i) + "\n"

                print err_msg
                print info_msg

                continue

            else:

                word_count = len(en_words_list)

                for j in range(word_count):
                    en_word = en_words_list[j].strip('[|]')
                    cn_word = cn_words_list[j].strip('[|]')

                    if len(cn_word) > cn_count_limit:
                        print cn_word
                        continue

                    if cn_word == en_word:
                        # print en_word
                        continue

                    en_cn_dict[en_word] = cn_word




def dumps_dict(dict_filename, en_cn_dict):

    with codecs.open(dict_filename, "w", "utf-8") as fd:
        for k, v in en_cn_dict.items():
            line = k + " : " + v + "\n"
            fd.write(line)



if __name__ == '__main__':

    en_cn_dict = {}
    file_list = list_dir("./result")

    for file in file_list:
        load_file(file, en_cn_dict, cn_count_limit=7)
        # break
    dumps_dict("en_cn_dict.text", en_cn_dict)