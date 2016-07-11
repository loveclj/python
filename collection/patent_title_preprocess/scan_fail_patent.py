#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: scan_fail_patent.py.py
@time: 4/28/16 10:05 AM
"""
import batch_get
import process
import codecs



if __name__ == '__main__':
    fail_pids = process.load_list('fail_pids.text')
    keys = []
    for pid in fail_pids:
        keys.append({'patent_id': {'S': pid}, 'lang': {'S': 'EN'} })

    attributes_to_get = ['patent_id', 'title']
    batch_getter = batch_get.BatchGet('patent_title', 'patent_id', 'lang', attributes_to_get)
    items = batch_getter.get_by_list(keys)

    fd = codecs.open('fail_pid2title.text', 'w', 'utf-8')
    for item in items:
        line = item[u'patent_id']['S'] + u":" + unicode(process.binary2string(item[u'title']['B']), "utf-8") + '\n'

        fd.write(line)

    fd.close()

