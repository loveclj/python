#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: translation_lambda.py
@time: 5/25/16 6:49 PM
"""

import json
import random
import md5
import urllib
import httplib

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


def lambda_handler(event, context):

    appid = '20151113000005349'
    secretKey = 'osubCEzlGjzvw8qdQc41'

    q = 'pie'
    fromLang = 'en'
    toLang = 'zh'

    print q

    translater = BaiduTranslation(Appid=appid, SecretKey=secretKey)

    response = translater.translate(src_lang=fromLang, dst_lang=toLang, q=q[:-2])

    print response











