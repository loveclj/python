#!/usr/bin/env python
# coding=utf-8

s = "中国"

try:
    ss = unicode(s, "ascii")
except:
    print "unicode error", s

print isinstance(s, unicode)
print s
