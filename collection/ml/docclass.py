__author__ = 'lizhifeng'

import re
import math

doc = "dog sex cat  bird  man cat"

def get_words(doc):
    splitter = re.compile('\\W*')
    words = [s.lower() for s in splitter.split(doc) if len(s) > 2 and len(s) < 20]
    dict ={}
    for w in words:
        dict[w] = 1

    return dict


class Classifier:
    def __init__(self, getfeatures, filename = None):
        self.fc = {}
        self.cc = {}

        self.getfeatures = getfeatures

    def incf(self, f, cat):
        self.fc.setdefault(f,{})
        self.fc[f].setdefault(cat,0)
        self.fc[f][cat] += 1

    def incc(self, cat):
        self.cc.setdefault(cat, 0)
        self.cc[cat] += 1

    def fcount(self,f, cat):
        if f in self.fc and  cat in self.fc[f]:
            return float(self.fc[f][cat])
        return 0.0

    def catcount(self,cat):
        if cat in self.cc:
            return  float(self.cc[cat])
        return 0

    def totalcount(self):
        return sum(self.cc.values())

    def categories(self):
        return self.cc.keys()

    def train(self, item, cat):
        features =  self.getfeatures(item)
        self.incf(features, cat)
        self.incc(cat)


