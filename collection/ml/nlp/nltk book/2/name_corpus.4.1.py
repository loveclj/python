__author__ = 'lizhifeng'

from nltk import FreqDist
from nltk import  ConditionalFreqDist
import  nltk.corpus

names = nltk.corpus.names
cfd = ConditionalFreqDist((fileid, name[-1])
                          for fileid in names.fileids()
                          for name in names.words(fileid))

cfd.plot()



