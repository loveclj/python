#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: query_solr.py
@time: 8/1/16 4:43 PM
"""


import urllib2
import urllib
import json


if __name__ == '__main__':
    query = "http://192.168.3.248:9088/patsnap/PATENT/EN_CN?" \
            "fl=_id,PN_STR&q=%28apple%29&sort=score%20desc,_version_%20desc,UniqueKey%20desc&wt=json&rows=1&cursorMark="

    query += urllib2.quote('*')
    print query
    content = urllib2.urlopen(query)
    res = content.read()
    res = json.loads(res)
    print res
    # print len(res['response']['docs'])
