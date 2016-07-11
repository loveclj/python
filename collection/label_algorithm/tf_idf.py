#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: tf_idf.py
@time: 3/22/16 11:38 AM
"""
import math


def tf_idf(patent2stem_freq):

    patent2norm_tf = {}
    stem2df = {}
    patent2stem_score = {}
    patent_count = 0
    for patent, stem_freq in patent2stem_freq.items():

        total_count = 0
        for stem, freq in stem_freq.items():
            total_count += freq

            if stem in stem2df.keys():
                stem2df[stem] += 1
            else:
                stem2df[stem] = 1

        if total_count == 0:
            continue

        norm_tf = {}
        for stem, freq in stem_freq.items():
            norm_tf[stem] = float(freq)/total_count

        patent2norm_tf[patent] = norm_tf
        patent_count += 1

    for patent, norm_tf in patent2norm_tf.items():
        stem_score = {}
        for stem, tf in norm_tf.items():
            stem_score[stem] = tf * math.log10(patent_count/stem2df[stem])

        patent2stem_score[patent] = stem_score

    return patent2stem_score


def cluster_score_acc(patent2stem_score, patent2cluster):
    cluster2stem_score = {}
    for patent, cluster in patent2cluster.items():
        if cluster not in cluster2stem_score.keys():
            cluster2stem_score[cluster] = {}

        if patent not in patent2stem_score.keys():
            continue

        for stem, score in patent2stem_score[patent].items():
            if stem in cluster2stem_score[cluster].keys():
                cluster2stem_score[cluster][stem] += score
            else:
                cluster2stem_score[cluster][stem] = score

    return cluster2stem_score


def dict_value_topk(dict, stem2term,  N):
    dict = sorted(dict.iteritems(), key=lambda d:d[1], reverse=True)

    i = 0
    topk = {}
    for k, v in dict:
        term = stem2term[k]
        topk[term] = v

        if i < N:
            i += 1
        else:
            break

    topk = sorted(topk.iteritems(), key=lambda d:d[1], reverse=True)

    return topk








if __name__ == '__main__':
    pass