#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: __init__.py.py
@time: 6/14/16 2:22 PM
"""


from __future__ import print_function

import  boto3
import  json
import  decimal
from boto3.dynamodb.conditions import Key, Attr



default_region = u'cn-north-1'
default_service = u'dynamodb'

# default_table = u'patent'

last_key_field = u'LastEvaluatedKey'


