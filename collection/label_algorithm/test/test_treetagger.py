#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: test_treetagger.py.py
@time: 3/23/16 5:04 PM
"""

import treetaggerwrapper as ttpw
p = ttpw.TaggerPoll()

res = []
text = "This is Mr John's own house, it's very nice."
print("Creating jobs")
for i in range(10):
    print("     Job", i)
    res.append(p.tag_text_async(text))
print("Waiting for jobs to be completed")
for i, r in enumerate(res):
    print("     Job", i)
    r.wait_finished()
    print(r.result)
p.stop_poll()
print("Finished")