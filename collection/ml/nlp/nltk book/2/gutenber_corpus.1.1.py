__author__ = 'lizhifeng'

from nltk.corpus import  gutenberg

for fileid in gutenberg.fileids():
    num_char = len(gutenberg.raw(fileid))
    num_word = len(gutenberg.words(fileid))
    num_sents = len(gutenberg.sents(fileid))
    num_vocab = len(set(w.lower() for w in gutenberg.words(fileid)))
    print (round(num_char/num_word), round(num_word/num_sents), round(num_word/num_vocab), fileid)
