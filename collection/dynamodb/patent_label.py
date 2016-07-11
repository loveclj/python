__author__ = 'lizhifeng'

import base64
import  binascii

import  boto3
from boto3.session import Session
from boto3.dynamodb.conditions import Key, Attr

session = Session(aws_access_key_id='anything',
                  aws_secret_access_key='anything',
                  region_name='us-east-1')

dynamodb = session.resource('dynamodb', endpoint_url='http://192.168.6.170:8000')

#client  = session.client('dynamodb', 'http://192.168.6.170:8000')


patent_table = dynamodb.Table("patent")
title_table  = dynamodb.Table("patent_title")
abstr_table  = dynamodb.Table("patent_abstract")

patent_id_fd = open("./conf/patent_id_file", "r")

uuids = patent_id_fd.readlines()

for uuid in uuids:
    print uuid.strip('\n')

    #get tiltle
    response =  title_table.query(
        KeyConditionExpression = Key('patent_id').eq("c562d4f6-6e59-4935-a9ac-b88653f9d613")
    )
    #print response

    title_base64 = response['Items'][0]['title']
    print type(title_base64)


    #title_base64 = binascii.b2a_hex(title_base64)
  #  print title_base64
   # title_gzip  = base64.b64decode(title_base64)
    #print title_gzip
    break



