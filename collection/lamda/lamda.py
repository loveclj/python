# encoding: utf-8


import boto3
import nltk
import re
import random
import time
import StringIO
import gzip
import base64
import codecs
import jieba
import md5
import urllib
import httplib
import json


# add nlt data path
nltk.data.path.append("./nltk_data")

# table name
patent_title_table = "landscape_title_test"
landscape_feature_table = "landscape_feature_sync"

# only support Chinese and English
en = "EN"
cn = "CN"

# English grammar for splitting sentence into phrase
grammar = "NP: {<NNS|NN|NNP|NNPS|JJ><NN|NNS>}"

# stopwords file
en_stopwords_path = "./enStopwords.text"
cn_stopwords_path = "./cnStopwords.text"

# Baidu translation API id
appid = '20151113000005349'
secretKey = 'osubCEzlGjzvw8qdQc41'


# check word is legal or not
def check_en_words(word, mode):
    if mode.match(word):
        return True
    else:
        return False


# load stop word from file
def load_list(filename="stopwords"):
    fd = codecs.open(filename, "r", "utf-8")
    lines = fd.readlines()
    words_list = []

    for line in lines:
        words_list.append(line.strip('\n'))

    words_set = set(words_list)
    fd.close()
    return words_set


# decode zip binary to string
def binary2string(encode):
    obj = StringIO.StringIO(encode)
    gzip_obj = gzip.GzipFile(fileobj=obj)
    decode = gzip_obj.read()
    gzip_obj.close()
    return decode


# Baidu Trainslation Object
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

        try:
            http_client = httplib.HTTPConnection('api.fanyi.baidu.com')
            http_client.request('GET', query_url)

            response = http_client.getresponse()

            result = response.read()

            result = json.loads(result)

            w = result["trans_result"][0]['dst']
            if w:
                return w
            else:
                return ""
        except Exception, e:
            print "translate fails:"
            return ""


def split_en_sentence_as_phrase(sentence, stopwords, parser, mode):

    try:
        phrases = ""
        sentence = sentence.replace(u'”', '')
        words = nltk.word_tokenize(sentence.lower())
        sentence_tagged = nltk.pos_tag(words)
        # print sentence_tagged

        sentence_split = parser.parse(sentence_tagged)

        lemmatize = nltk.stem.WordNetLemmatizer().lemmatize

        for node in sentence_split:

            if type(node) is nltk.Tree:
                words = []
                for sub_node in node:
                    if sub_node[0] not in stopwords and check_en_words(sub_node[0], mode):
                        words.append(sub_node[0])

                if words:
                    words[-1] = lemmatize(words[-1])
                    phrases += u" ".join(words).upper() + u";"
            else:
                if node[0] not in stopwords and check_en_words(node[0], mode):
                    w = lemmatize(node[0]).upper()
                    if len(w) >= 4:
                        phrases += w + u";"
                else:
                    pass
        return phrases
    except:
        print "[Error] split sentence fails: ", sentence
        return ""


def split_cn_sentence_as_phrase(sentence, stopwords, filter_mode):

        result = ""

        try:
            words = jieba.cut(sentence, cut_all=False)
            seg_list = []
            for word in words:

                if len(word) < 2 or len(word) > 6 or word in stopwords or filter_mode.match(word):
                    continue

                seg_list.append(word)

            result = u";".join(seg_list)
        except:
            print "[Error]: split cn sentence fail, sentence:", sentence

        return result


def lambda_handler(event, context):
    
    items = []

    # parse patent_id, lang and title from stream record
    for record in event['Records']:

        if record['eventName'] != 'REMOVE':
            try:
                patent_id = record['dynamodb']['Keys']['patent_id']['S']

                lang = record['dynamodb']['Keys']['lang']['S']

                title_binary = record['dynamodb']["NewImage"]['title']['B']
                title_zipped = base64.decodestring(title_binary)
                title = binary2string(title_zipped)

                item = (patent_id, lang, title)

                items.append(item)
            except:
                print "[Error] failed to extract info from record"
                print record

    client = boto3.client('dynamodb')
    en_stopwords = load_list(en_stopwords_path)
    cn_stopwords = load_list(cn_stopwords_path)

    parser = nltk.RegexpParser(grammar)

    # en word only contain number, character, and hyphen
    en_mode = re.compile("[a-zA-Z0-9][a-zA-Z0-9-]+$")

    cn_filter_mode = re.compile(r'[0-9]+$')

    from_lang = 'en'
    to_lang = 'zh'

    # init Baidu Translator
    translater = BaiduTranslation(Appid=appid, SecretKey=secretKey)

    for item in items:
        
        patent_id = item[0]
        lang = item[1]
        title = item[2]

        label_en = ""
        label_cn = ""

        # split en title, and translate  en phrase into cn phrase
        if lang.upper() == en:

            label_en = split_en_sentence_as_phrase(sentence=title, parser=parser, mode=en_mode, stopwords=en_stopwords)

            if label_en == u"":
                continue

            label_en_list = label_en.split(u";")
            label_cn_list = []

            for w in label_en_list:
                if not w:
                    continue

                response = translater.translate(src_lang=from_lang, dst_lang=to_lang, q=w)
                if response != u"" and response not in cn_stopwords:
                    label_cn_list.append(response)

            label_cn = u";".join(label_cn_list)

        elif lang.upper() == cn:  # spilt cn title into phrase
            label_cn = split_cn_sentence_as_phrase(sentence=title, stopwords=cn_stopwords, filter_mode=cn_filter_mode)
        else:  # ignore other lang
            continue

        # no label to update
        if label_cn == u"" and label_en == u"":
            continue

        current_time_in_ms = int(time.time() * 1000)

        expression_attributes_values = {}

        # update updated timestamp as current time,
        # if created timestamp is existed, no update, otherwise set it as  current time
        update_expression = u"SET updated_ts=:val3, created_ts = if_not_exists(created_ts, :val3)"

        # add cn label, if  label_cn is translated from en, no update if label_cn exists
        if lang.upper() == en and label_cn != u"":
            update_expression += u", label_cn = if_not_exists(label_cn, :val1)"
            expression_attributes_values[u":val1"] = {u"S": label_cn}
        elif lang.upper() == cn and label_cn != u"":
            update_expression += u", label_cn=:val1"
            expression_attributes_values[u":val1"] = {u"S": label_cn}

        # add en label
        if label_en:
            update_expression += u", label_en=:val2"
            expression_attributes_values[u":val2"] = {u"S": label_en}

        # update version, add 1 to version, if version doesn't exist, set it as 1
        update_expression += u" ADD version  :val4"

        expression_attributes_values[u":val3"] = {u"S": str(current_time_in_ms)}
        expression_attributes_values[u":val4"] = {u"N": u"1"}

        # update item
        response = ""
        try:
            response = client.update_item(TableName=landscape_feature_table,
                                      Key={u'patent_id': {u'S': patent_id}},
                                      UpdateExpression=update_expression,
                                      ExpressionAttributeValues=expression_attributes_values)
        except:
            print "[Error] update table fails:", response
    
    return 0


# if __name__ == "__main__":
#     record = {u'eventID': u'eb8c4acbbf112f62c4fa40383ef40fcc', u'eventVersion': u'1.1', u'dynamodb': {u'SequenceNumber': u'9624400000000004552440999', u'Keys': {u'lang': {u'S': u'CN'}, u'patent_id': {u'S': u'8a3f39dfe8104360b03d036ca4dee45m'}}, u'SizeBytes': 140, u'NewImage': {u'lang': {u'S': u'CN'}, u'title': {u'B': u'H4sIAAAAAAAAAHs+c+/L1klA9Hzytvd7Op7s6nm/pxMAvuVndxUAAAA='}, u'patent_id': {u'S': u'8a3f39dfe8104360b03d036ca4dee45m'}}, u'ApproximateCreationDateTime': 1464233820.0, u'StreamViewType': u'NEW_AND_OLD_IMAGES'}, u'awsRegion': u'us-east-1', u'eventName': u'INSERT', u'eventSourceARN': u'arn:aws:dynamodb:us-east-1:006694404643:table/landscape_title_test/stream/2016-05-24T02:32:46.876', u'eventSource': u'aws:dynamodb'}
#     record = {u'eventID': u'b08a9ec23718b71c8253aca1ec9723c7', u'eventVersion': u'1.1', u'dynamodb': {u'OldImage': {u'lang': {u'S': u'EN'}, u'title': {u'B': u'H4sIAAAAAAAAAHs+c+/L1klA9Hzytvd7Op7s6nm/pxMAvuVndxUAAAA='}, u'patent_id': {u'S': u'8a3f39dfe8104360b03d036ca4dee45m'}}, u'SequenceNumber': u'9624500000000004552815956', u'Keys': {u'lang': {u'S': u'EN'}, u'patent_id': {u'S': u'8a3f39dfe8104360b03d036ca4dee45m'}}, u'SizeBytes': 289, u'NewImage': {u'lang': {u'S': u'EN'}, u'title': {u'B': u'H4sIAAAAAAAAAEXMwQ2AIBBE0VamAJrYwIhEZMmyaui/ETUePP+ft9NXTQGDdpaWkdloUtElbnSYpKJfjMQ4eldzNE0MkJYw5nDuWNSeqTL6a8ivifOSeQOkuKyWZQAAAA=='}, u'patent_id': {u'S': u'8a3f39dfe8104360b03d036ca4dee45m'}}, u'ApproximateCreationDateTime': 1464234600.0, u'StreamViewType': u'NEW_AND_OLD_IMAGES'}, u'awsRegion': u'us-east-1', u'eventName': u'MODIFY', u'eventSourceARN': u'arn:aws:dynamodb:us-east-1:006694404643:table/landscape_title_test/stream/2016-05-24T02:32:46.876', u'eventSource': u'aws:dynamodb'}
#     event = {"Records": [record]}
#     lambda_handler(event, None)