#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: update.py
@time: 6/12/16 5:11 PM
"""
import boto3

key = {
  "job_id": {"S":"test"},

  "job_sequence": {"N": "0"},
      "error_code": {"N": "200"},

  "job_param": {"M": {
    "lang": {"S": "EN"},
    "query": {"S": "car"},
    "query_type": {"S": "solr"},
    "rows": {"N": "10000"}
  }},
  "job_status": {"S": "SUCCESS"},

}

attribute = {

  "error_code": {"N": "200"},

  # "job_param": {"M": {
  #   "lang": {"S": "EN"},
  #   "query": {"S": "car"},
  #   "query_type": {"S": "solr"},
  #   "rows": {"N": "10000"}
  # }},
  "job_status": {"S": "SUCCESS"},

}

client = boto3.client('dynamodb')

client.put_item(TableName='landscape', Item=key) #, ExpressionAttributeValues=attribute)


if __name__ == '__main__':
    pass