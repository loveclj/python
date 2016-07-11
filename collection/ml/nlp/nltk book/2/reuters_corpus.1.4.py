__author__ = 'lizhifeng'

from nltk.corpus import reuters

print reuters.fileids()

# ategories in the Reuters corpus overlap with each other,
#  simply because a news story often covers multiple topics.
#  We can ask for the topics covered by one or more documents,
# or for the documents included in one or more categories.
#  For convenience, the corpus methods accept a single fileid or a list of fileids.
print reuters.categories()
print reuters.categories("test/14826")
print reuters.fileids(["cpu", "gpu"])


print  reuters.words("test/14826")
