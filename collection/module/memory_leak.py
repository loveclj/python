__author__ = 'lizhifeng'

import gc

gc.set_debug(gc.DEBUG_STATS|gc.DEBUG_LEAK)


class A:
    def __del__(self):
        del self.b

class B:
    def __del__(self):
         del self.a

if __name__ == "__main__":
    a = A()
    b = B()
    a.b = b
    b.a = a

    del a
    del b

    print "gc.collect:", gc.collect()
    print "gc.garbage:", gc.garbage
