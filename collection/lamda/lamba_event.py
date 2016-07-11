#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: lamba_event.py
@time: 5/24/16 10:49 AM
"""

import boto3
import uuid

import StringIO
import gzip
import base64

def gzipstring(raw):
    out = StringIO.StringIO()
    with gzip.GzipFile(fileobj=out, mode="w") as f:
        f.write(raw)

    return out.getvalue()

    return s
def binary2string(encode):
    obj = StringIO.StringIO(encode)
    gzip_obj = gzip.GzipFile(fileobj=obj)
    decode = gzip_obj.read()
    gzip_obj.close()
    return decode


table_name = "landscape_title_test"


def insert_table(title, lang):

    client = boto3.client('dynamodb')

    patent_id = uuid.uuid4().hex
    patent_id = "8a3f39dfe8104360b03d036ca4dee45m"
    item = {
        "patent_id": {"S": patent_id},
        "lang": {"S": lang},
        "title": {"B": title}
    }

    response = client.put_item(TableName=table_name,
                    Item=item)

    print response


if __name__ == '__main__':
    binary = base64.decodestring("H4sIAAAAAAAAAEXMwQ2AIBBE0VamAJrYwIhEZMmyaui/ETUePP+ft9NXTQGDdpaWkdloUtElbnSYpKJfjMQ4eldzNE0MkJYw5nDuWNSeqTL6a8ivifOSeQOkuKyWZQAAAA==")
    # binary = base64.decodestring("H4sIAAAAAAAAAHs+c+/L1klA9Hzytvd7Op7s6nm/pxMAvuVndxUAAAA=")
    # insert_table(title=binary, lang="EN")

    binary = base64.decodestring("H4sIAAAAAAAAAHs+c+/L1klA9Hzytvd7Op7s6nm/pxMAvuVndxUAAAA=")
    insert_table(title=binary, lang="CN")
