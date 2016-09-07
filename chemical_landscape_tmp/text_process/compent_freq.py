#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: compent_freq.py
@time: 7/11/16 10:40 AM
"""

import fileIO.dumps

def load_id_compent_from_file(filename):
    id_compent = {}
    fd = open(filename, 'r')
    while True:
        line = fd.readline()
        if not line:
            break

        try:
            l = line.strip('\n').replace('\t', ' ').split(' ')

            print l
            id = l[0]

            n = int(id)
            compent = " ".join(l[1:])
            id_compent[id] = compent
        except:
            continue

    return id_compent


def cmp(a, b):
    # print a[-1], b[-1], a[-1] > b[-1]
    return int(a[-1]) - int(b[-1])



if __name__ == '__main__':
    compent_freq = fileIO.dumps.load_map_from_file('../df.text', ',')
    for k, v in compent_freq.items():
        print k, v
        pass
    id_compent = load_id_compent_from_file('../puchem_descr.text')
    total_items = 425651
    dimension = 881

    outfile = "id_freq_describe.text"
    fd = open(outfile, 'w')

    # for k, v in id_compent.items():
    for k in range(dimension):
        k = str(k)
        if k not in compent_freq.keys():
            print k

        freq = int(compent_freq[k])
        p = str(float(freq)/total_items)

        line = k + ':' + p + ":" + id_compent[k] + '\n'
        print line,
        fd.write(line)

    fd.close()

    outfile = "id_freq_describe_sorted.text"
    fd = open(outfile, 'w')

    items = sorted(compent_freq.items(), cmp=cmp, reverse=True)

    for item  in items:
        id = item[0]
        freq = int(item[1])
        descr = id_compent[id]

        freq = str(float(freq)/total_items)
        line = id + ":" + freq + ":" + descr + "\n"
        print line,
        fd.write(line)

    fd.close()



