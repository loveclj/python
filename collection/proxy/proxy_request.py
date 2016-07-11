#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: proxy_request.py
@time: 5/13/16 11:26 AM
"""

import urllib2
import json

import translation

class Proxy:

    def __init__(self, url):
        self.url = url
        self.proxy_list = []

    def get_proxy_list(self):
        context = urllib2.urlopen(self.url).read()

        proxy_map = json.loads(context)


        for e in proxy_map:
            proxy = e["host"] + ":" + str(e["port"])
            self.proxy_list.append(proxy)


    def switch(self):
        while True:
            if not self.proxy_list:
                self.get_proxy_list()
                continue

        proxy = self.proxy_list[0]
        print proxy
        self.proxy_list.remove(proxy)

        opener = urllib2.build_opener(urllib2.ProxyHandler({"http": proxy}))
        urllib2.install_opener(opener)

    def request(self, q):

            try:
                request = urllib2.urlopen("http://www.baidu.com").read()
                print request
            except:
                pass









if __name__ == '__main__':


    appid = '20151113000005349'
    secretKey = 'osubCEzlGjzvw8qdQc41'

    q = 'pie'
    fromLang = 'en'
    toLang = 'zh'

    words = translation.load_word_freq("en_word_freq.text")

    # 9448295
    print len(words)


    translater = translation.BaiduTranslation(Appid=appid, SecretKey=secretKey)

    proxy = Proxy("http://qsrdk.daili666api.com/ip/?tid=556363427011886&num=2&format=json")
    proxy.request("a")
