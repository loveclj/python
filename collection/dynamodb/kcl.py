__author__ = 'lizhifeng'


def decrator(func):
    def f():
        print "hello"
        func()
        print "world"

    return f

@decrator
def he():
    print "---"

he()