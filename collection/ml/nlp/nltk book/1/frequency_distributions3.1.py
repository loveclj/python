# __author__ = 'lizhifeng'
from nltk import  FreqDist
from nltk.book import text3, text4
from nltk import FreqDist
from nltk import bigrams

fdfist1 = FreqDist(text3)
print fdfist1
print fdfist1.most_common(50)

freq = FreqDist(text3)
v = set(text3)
long_words = [w for w in v if len(w) >  13  and freq[w]]
print long_words

# bigrams
print list(bigrams(long_words))
print list(bigrams(text3))

# llocations are essentially just frequent bigrams,
# except that we want to pay more attention to the cases that involve rare words.
#  In particular, we want to find bigrams that occur more often
# than we would expect based on the frequency of the individual words.
print "----"
print text4.collocations()
print "----"
