#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: noun_phrase.py
@time: 6/29/16 3:41 PM
"""


import textblob
import codecs


def extract_np(text):
    blob = textblob.TextBlob(text)
    return blob.noun_phrases


if __name__ == '__main__':
    text = "data center cooling system"

    outfile = "./pid2nps.text"
    ofd = codecs.open(filename=outfile, mode='w', encoding='utf-8')
    i = 0

    with codecs.open(filename="../data/abstract.text", mode="r", encoding='utf-8') as fd:
        while True:
            line = fd.readline().strip('\n')
            if not line:
                break

            l = line.split(":")
            pid = l[0]
            abstr = u".".join(l[1:])
            # print abstr
            nps = extract_np(abstr)
            line = pid + ":" + u",".join(nps) + "\n"
            ofd.write(line)

            i += 1
            if i % 1000 == 0:
                print i

    ofd.close()
    print "Done! "