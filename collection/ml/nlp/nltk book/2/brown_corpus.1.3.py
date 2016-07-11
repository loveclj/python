__author__ = 'lizhifeng'

from nltk.corpus import brown
import nltk

print brown.categories()

print brown.words(categories="news")

cfd = nltk.ConditionalFreqDist((genre, word)
                               for genre in brown.categories()
                               for word in brown.words(categories=genre))

genres = ["news", "religion", "hobbies", "humor"]
modals = ["can", "could", "must"]

cfd.tabulate(conditions=genres, samples=modals)
cfd.plot(conditions=genres, samples=modals)