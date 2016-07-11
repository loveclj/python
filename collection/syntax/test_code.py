#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: test_code.py.py
@time: 1/27/16 10:59 AM
"""

import sys
if __name__ == '__main__':
    print sys.getdefaultencoding()
    print sys.getfilesystemencoding()

    a = '中国'
    print a
    c = a.decode('utf-8').encode('gb2312').decode("gb2312")
    print type(c)

    b = u'中国'
    print b

    # print a.encode('gb2312')