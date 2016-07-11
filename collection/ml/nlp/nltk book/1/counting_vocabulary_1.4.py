from __future__ import  division
import nltk
from nltk.book import text3




# get count of words in text3
print len(text3)

# obtain the vocabulary items of text
print set(text3)


def lexical_diversity(text):
    return len(set(text)) / len(text)


def percentage(target, text):
    return 100 * text.count(target) / len(text)


print lexical_diversity(text3)
print percentage("many", text3)
