__author__ = 'lizhifeng'
import gc
import sys

gc.set_debug(gc.DEBUG_STATS|gc.DEBUG_LEAK)

a = []
b = []
a.append(b)
b.append(a)
print a is b
print 'a refcount:', sys.getrefcount(a)
print b
print 'b refcount:', sys.getrefcount(b)

del a
del b
print 'gc.collect', gc.collect()
