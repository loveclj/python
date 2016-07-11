__author__ = 'lizhifeng'
from nltk.corpus import  swadesh

print swadesh.fileids()
print swadesh.words('en')

fr2en = swadesh.entries(['fr', 'en'])
print fr2en

translate = dict(fr2en)
print translate["chien"]