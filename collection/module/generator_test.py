__author__ = 'lizhifeng'

def my_range(n):
    i = 0
    while i < n:
        yield i
        i += 1

generator = my_range(10)

print generator.next()
print generator.next()


