__author__ = 'lizhifeng'

import time
import gc

gc.disable()
start = time.time()
data = range(1, 4000000)
wdict = dict(zip(data, data))

print time.time() - start
gc.enable()

del start
del data
del wdict


start = time.time()
data = range(1, 4000000)
wdict = dict(zip(data, data))

print time.time() - start



