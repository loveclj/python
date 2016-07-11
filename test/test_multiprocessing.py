#!/usr/bin/env python
# coding=utf-8
import time
import multiprocessing

def process_fun(n):
    time.sleep(n)
    print "sleep over ", n


process_num = 4
for k in range(10):
    pool =  multiprocessing.Pool(process_num)

    for i in range(process_num*2):
        pool.apply_async(process_fun, (1,))
        # pool.apply_async(process_fun, (i,))

    print "main process over"

pool.close()
pool.join()




