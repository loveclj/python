#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: text_pretty.py
@time: 7/12/16 5:19 PM
"""


if __name__ == '__main__':
    filename = "./id_freq_describe_sorted.text"
    out_filename = "puchemID_ratio_descr.text"

    length = 10

    with open(filename, 'r') as in_fd, open(out_filename, 'w') as out_fd:
        while True:
            line = in_fd.readline()
            if not line:
                break

            print line
            l = line.strip('\n').split(':')
            id = l[0]
            p = l[1]
            descr = "".join(l[2:])


            p = float(p) * 100
            p = str(p)
            percent = " "
            if len(p) > length:
                percent += p[:length] + "%"
            else:
                percent += p + "%" + " "*(length - len(p))

            id = id + " " * (3 - len(id))

            line = id + ":" + percent + ": " + descr + '\n'

            out_fd.write(line)

