__author__ = 'lizhifeng'

from nltk.corpus import PlaintextCorpusReader

corpus_root = "./t"
wordlist = PlaintextCorpusReader(corpus_root, '.*')
print wordlist.fileids()
print wordlist.words("connectives")
