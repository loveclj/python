#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: main.py.py
@time: 3/21/16 1:48 PM
"""
import json
import nltk
import text_process
import tf_idf
from text_process import *
from Error import Error
import extract_nn

class JobInfo(object):
    def __init__(self, info):
        try:
            self.grid2cluster = info["cluster_map"]
            self.nCluster = info["cluster_num"]
            self.grid_nCol = info["col_num"]
            self.grid_nRow = info["row_num"]
            self.nPatent = info["patent_count"]
            self.patent2grid_chunk_id = info["patent_map_chunk_id"]
            self.patent2grid_chunk_count = info["patent_map_chunk_count"]
            self.job_status = info["job_status"]
            self.job_id = info["job_id"]
            self.patent2grid = {}
            self.patent2cluster = {}
            if self.job_status != "SUCCESS":
                raise Error("job fails")
        except Error as e:
            print e.value
        except:
            print "parse landscape job info error"
        finally:
            pass

    def get_patent2cluster(self):

        for patent, grid in self.patent2grid.items():
            cluster = self.grid2cluster[grid]

            self.patent2cluster[patent] = cluster

        return self.patent2cluster


def parse_patent2grid(content):
    patent2grid_list = content.split(',')
    patent2grid = {}
    for e in patent2grid_list:
        kv = e.split(':')
        patent2grid[kv[0]] = kv[1]

    return patent2grid

if __name__ == '__main__':

    landscape_table = dynamodb.Table(table_name="landscape_test",
                               partition_key='job_id',
                               sort_key='job_sequence')

    item = landscape_table.get_item(partition_key='1b1af798-e0a7-4ce7-80fa-d8d8916b47ed', sort_key=0)[u'Item']
    job_info = JobInfo(item)
    # print item

    patent2grid_table =dynamodb.Table(table_name='landscape_patent_map_data_test',
                                partition_key='patent_map_chunk_id',
                                sort_key='n')
    item = patent2grid_table.get_item(partition_key=job_info.patent2grid_chunk_id, sort_key=0)

    patent2grid_str = gzip.decompress(item[u'Item'][u'content'])
    # print patent2grid_str

    job_info.patent2grid = parse_patent2grid(patent2grid_str)
    # print job_info.patent2grid

    patent2cluster = job_info.get_patent2cluster()
    # print patent2cluster

    # save begin
    #
    # save_title_abstr_to_text(patent2cluster.keys(), title_table_name='patent_title',
    #                          abstr_table_name='patent_abstract')
    # patent2title, patent2abstr = get_title_abstr_from_dynamodb(patent2cluster.keys(),
    # title_table_name='patent_title', abstr_table_name='patent_abstract')
    #
    # patent2title, patent2abstr =load_tiltle_abstr_from_text()
    # print patent2title
    # print patent2abstr
    #
    # patent2title_stem_freq, title_stem_freq, patent2abstr_stem_freq, abstr_stem_freq, stem2term = text_process.get_stem_freq(patent2title, patent2abstr)
    # text_process.save_dict(title_stem_freq, "title_freq")
    # text_process.save_dict(abstr_stem_freq, "abstr_freq")
    # text_process.save_dict_dict(patent2abstr_stem_freq, "patent_abstr_stem_freq")
    # text_process.save_dict_dict(patent2title_stem_freq, "patent_title_stem_freq")
    # text_process.save_dict(stem2term, "stem2term")

    # save end

    title_stem_freq = load_dict("title_freq")
    abstr_stem_freq = load_dict("abstr_freq")
    patent2abstr_stem_freq = load_dict_dict("patent_abstr_stem_freq")
    patent2title_stem_freq = load_dict_dict("patent_title_stem_freq")
    stem2term = load_dict("stem2term")

    # print title_stem_freq
    # print abstr_stem_freq
    # print patent2title_stem_freq

    patent2descr_stem_score = tf_idf.tf_idf(patent2abstr_stem_freq)
    patent2title_stem_score = tf_idf.tf_idf(patent2title_stem_freq)

    patent2stem_score = {}
    for patent, stem_score in patent2descr_stem_score.items():
        if patent not in patent2stem_score.keys():
            patent2stem_score[patent] = {}

        for k, v in stem_score.items():
            if k in patent2stem_score[patent].keys():
                patent2stem_score[patent][k] += v
            else:
                patent2stem_score[patent][k] = v

    # for patent, stem_score in patent2title_stem_score.items():
    #     if patent not in patent2stem_score.keys():
    #         patent2stem_score[patent] = {}
    #
    #     for k, v in stem_score.items():
    #         if k in patent2stem_score[patent].keys():
    #             patent2stem_score[patent][k] += v
    #         else:
    #             patent2stem_score[patent][k] = v

    # patent2stem_score = tf_idf.tf_idf(patent2title_stem_freq)

    text_process.save_dict(patent2stem_score, "score")

    # print patent2stem_score

    cluster2stem_score = tf_idf.cluster_score_acc(patent2stem_score, patent2cluster)

    sort_cluster_socre = {}
    # print patent2cluster
    # print job_info.grid2cluster
    for c, stem_score in cluster2stem_score.items():
        sort_cluster_socre[c] = tf_idf.dict_value_topk(stem_score, stem2term, 20)

    text_process.save_dict(sort_cluster_socre,  "cluster_score")
    # text_process.save_dict(cluster2stem_score, "cluster_score")

    label_table = dynamodb.Table2(table_name='landscape_label_test', partition_key='job_id')
    item = label_table.get_item(partition_key=job_info.job_id)

    #
    fd = open("label_keywords_topk20", 'r')
    original_label = json.load(fd)
    # print label_table.update_item(job_info.job_id, "text_label", label["text_label"])
    label_json = {}

    job_info.cluster2center = {}
    print original_label["text_label"]

    for grid in original_label["text_label"].keys():
        print type(grid)
       # grid = eval(grid)
        print job_info.grid2cluster.keys()
        if grid in job_info.grid2cluster.keys():

            cluster = job_info.grid2cluster[grid]
            job_info.cluster2center[cluster] = grid

    print job_info.cluster2center
    print job_info.grid2cluster
    lemmatize = nltk.WordNetLemmatizer().lemmatize
    for c, stem_score in sort_cluster_socre.items():

        c = str(job_info.cluster2center[c])
        label_str = ""
        print stem_score
        for kv in stem_score:
            try:
                label_str += lemmatize(kv[0]).upper() + ";"
            except:
                pass
        label_json[c] = label_str

    # use np method
    np_patent2keywords = extract_nn.load_key2list(filename="./test/patent2keywords.text")

    np_cluster2keywords_freq = {}

    for patent, keywords in np_patent2keywords.items():
        cluster = job_info.patent2cluster[patent]
        if cluster not in np_cluster2keywords_freq.keys():
            np_cluster2keywords_freq[cluster] = {}

        for keyword in keywords:
            keyword = keyword.lower()
            if not keyword:
                continue
            else:
                split_key_words = keyword.split(' ')
                if len(split_key_words) == 1:
                    keyword = lemmatize(split_key_words[0])
                else:
                    keyword = ""
                    for word in split_key_words[:-1]:
                        keyword += word + " "
                    keyword += lemmatize(split_key_words[-1])

            if keyword in np_cluster2keywords_freq[cluster].keys():
                np_cluster2keywords_freq[cluster][keyword] += 1
            else:
                np_cluster2keywords_freq[cluster][keyword] = 1

    np_cluster_label = {}
    patent_stop_words = text_process.load_list()
    print patent_stop_words

    for cluster, keyword_freq in np_cluster2keywords_freq.items():
        cluster = job_info.cluster2center[cluster]
        topk = sorted(keyword_freq.iteritems(), key=lambda d:d[1], reverse=True)
        print topk
        label = ""
        for k in topk:
            if k[0].lower() in patent_stop_words:
                print k[0]

                continue
            label += k[0].upper() +";"

        np_cluster_label[str(cluster)] = label



   # print label_table.update_item(job_info.job_id, "text_label", label_json)
    print label_table.update_item(job_info.job_id, "text_label", np_cluster_label)

    text_field = item['Item']['text_label']


    cluster2stem_tf_top20 = {}
    for c, labels in text_field.items():
        c = job_info.grid2cluster[c]
        cluster2stem_tf_top20[c] = labels

    for i in range(job_info.nCluster):
        if i not in cluster2stem_tf_top20.keys():
            continue

        print i, cluster2stem_tf_top20[i].lower()











