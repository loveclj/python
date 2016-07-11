__author__ = 'lizhifeng'

import  nltk

entries = nltk.corpus.cmudict.entries()
print len(entries)

for entry in entries:
    print entry
