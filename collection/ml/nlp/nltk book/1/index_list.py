__author__ = 'lizhifeng'

from nltk.book import text3

print text3.index("a")
print text3[100]

print text3
print isinstance(text3, list)

list_test = range(10)
print list_test
list_test[1:5] = [0]
print list_test