

from __future__ import print_function

import  boto3
import  json
import  decimal
from boto3.dynamodb.conditions import Key, Attr

import boto3


region  = u'cn-north-1'
service = u'dynamodb'
table   = u'patent'
field   = u'patent_id'

key_field = u'LastEvaluatedKey'

client = boto3.client(service, region)
response = client.scan(TableName = table, ProjectionExpression = field)

try:
        lastkey = response[key_field]
except:
        lastkey = []

while lastkey != []:
        print lastkey
        try:
                response = client.scan(TableName = table, ProjectionExpression = field, ExclusiveStartKey = lastkey)
                lastkey = response[key_field]
                patents = response[u'Items']
                for patent in patents:
                        print patent[field][u'S']
        except:
                lastkey = []

