#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: baidu_translation_api.py
@time: 4/28/16 4:58 PM
"""
import httplib
import md5
import urllib
import random
import codecs

import time

import gc

import commands

import json


class BaiduTranslation(object):
    def __init__(self, Appid, SecretKey):
        self.appid = Appid
        self.secret_key = SecretKey
        self.url = '/api/trans/vip/translate'


    def translate(self, src_lang, dst_lang, q):
        salt = random.randint(32768, 65536)
        sign = self.appid + q + str(salt) + self.secret_key

        engine = md5.new()
        engine.update(sign)
        sign = engine.hexdigest()

        query_url = self.url + '?appid=' + self.appid + '&q=' + urllib.quote(q) + \
                    '&from=' + src_lang + '&to=' + dst_lang + '&salt=' + str(salt) + '&sign=' + sign

        httpClient = None


        try:
            httpClient = httplib.HTTPConnection('api.fanyi.baidu.com')
            httpClient.request('GET', query_url)
 
            #response是HTTPResponse对象
            response = httpClient.getresponse()

            result = response.read()
            # print result

            result = json.loads(result)
            if not result["trans_result"][0]['dst']:
                print q
            return result["trans_result"][0]['dst']

        except Exception, e:
            print e
        finally:
            if httpClient:
                httpClient.close()


def get_file_list(directionay):
    cmd = "ls "  + directionay
    status, output = commands.getstatusoutput(cmd)
    print output.split()
    return output.split()




def get_pid2keywords_from_file(filename):
    pid2keywords = {}
    fd = codecs.open(filename, "r", 'utf-8')
    lines = fd.readlines()
    for line in lines:
        pk = line.split(u":")
        print pk
        pid = pk[0]
        keywords = pk[1].split(',')
        pid2keywords[pid] = keywords

    return pid2keywords

def get_word_freq():
    directionary = "/home/lizhifeng/sourceCode/pycharm/patent_title_preprocess/first_result_lang_en_env_cn/result"

    file_list = get_file_list(directionary)

    keyword_freq = {}
    words_set = set()

    for f in file_list:

        start = time.time()
        file = directionary + "/" + f
        fd = codecs.open(file, "r", "utf-8")
        lines = fd.readlines()


        for line in lines:
        # while True:

            line = line.strip('\n')

            if not line:
                break

            try:
                keywords = line.split(":")[1].split(',')
                for w in keywords:
                    if w in words_set:
                        keyword_freq[w] += 1

                    else:
                        keyword_freq[w] = 1
                        words_set.add(w)
            except:
                print line

        print f
        print "excute time", time.time() - start


        fd.close()

    fd = codecs.open("en_word_freq.text", "w", "utf-8")
    for k, v  in keyword_freq.items():
        line = k + u":" + str(v) + u"\n"
        fd.write(line)

    fd.close()


def load_word_freq(filename):

    words = []
    with open(filename, "r") as fd:
        for line in fd.readlines():
            word, freq = line.strip('\n').split(':')

            if len(word) > 2:
                words.append(word)

    return words




if __name__ == "__main__":

    appid = '20160525000022041'
    secretKey = 'TXeA_sksH2M0Ygcyhq_1'

    # pid2keywords = get_pid2keywords_from_file("24362339.text")
    q = 'pie'
    fromLang = 'en'
    toLang = 'zh'

    # words = load_word_freq("en_word_freq.text")

    # 9448295
    # print len(words)


    translater = BaiduTranslation(Appid=appid, SecretKey=secretKey)
    response = translater.translate(src_lang='en', dst_lang='zh', q=q)
    print response



    # q = "car; moto car; good; apple; kill; tud; he is jack, tom is there;therapeuticradiolabeled"
    # translater.translate(src_lang='en', dst_lang='zh', q=q)
    #
    n = 0
    start = time.time()

    k = 0
    q = ""
    for w in words:
        # print w,
        n += 1
        q += w + ";"
        k += 1

        if n < 100:
            continue
        else:
            response = translater.translate(src_lang='en', dst_lang='zh', q=q[:-2])
            word_translated_list = response[:-2].split(u'；')
            count = len(word_translated_list)

            src_words = q.split(";")

            if count == n:
                # print word_translated_list
                q = ""
            else:
                # print q
                # print response
                # print n
                # print count
                q = ""

                # break

            n = 0



        if k %1000 == 0:
            print time.time() - start
            start = time.time()





    

