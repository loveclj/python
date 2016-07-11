import urllib2
from nltk import word_tokenize
import nltk

url = u"http://www.gutenberg.org/files/2554/2554.txt"

# set proxy
proxies = {'http': 'http://www.someproxy.com:3128'}
urllib2.ProxyHandler(proxies)

# open url
response = urllib2.urlopen(url)

raw = response.read().decode('utf-8')

print type(raw)
print len(raw)
print raw[:75]

tokens = word_tokenize(raw)
print type(tokens)
print len(tokens)

text = nltk.Text(tokens)
type(text)
print text[1:9]

collocations = text.collocations()
print collocations




