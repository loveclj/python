#!/usr/bin/env python
# coding=utf-8

import jieba
import jieba.posseg as pseg

sentence = u"数据中心制冷系统"
sentence = u"得克萨斯州大学系统董事会"
sentence = u"使用人源化抗CD19嵌合抗原受体治疗癌症"
sentence = u"一种嵌合抗原受体hCD87-CAR及载有hCD87-CAR基因结构的慢病毒及质粒及其应用"

words = pseg.cut(sentence)

for w in words:
    print w.word, w.flag


seg_list = jieba.cut(sentence, cut_all=True)
print "Full mode: " + "/".join(seg_list) 


seg_list = jieba.cut(sentence, cut_all=False)
print "Default mode: " + "/".join(seg_list) 

seg_list = jieba.cut(sentence)
print "Accurracy mode: " + "/".join(seg_list) 
