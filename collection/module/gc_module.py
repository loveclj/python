#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: gc_module.py.py
@time: 1/26/16 1:25 PM
"""

import gc

# module description: https://docs.python.org/2.7/library/gc.html

# This module provides an interface to the optional garbage collector.
# It provides the ability to disable the collector, tune the collection frequency,and set debugging options.
# It also provides access to unreachable objects that the collector found but cannot free.
# Since the collector supplements the reference counting already used in Python,
# you can disable the collector if you are sure your program does not create reference cycles.
# Automatic collection can be disabled by calling gc.disable().
# To debug a leaking program call gc.set_debug(gc.DEBUG_LEAK).
# Notice that this includes gc.DEBUG_SAVEALL,
#  causing garbage-collected objects to be saved in gc.garbage for inspection.

if __name__ == '__main__':
    print gc.enable()
    print gc.isenabled()
    print gc.disable()
    print gc.get_threshold()