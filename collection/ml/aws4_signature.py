from boto3.session import Session
#coding=utf-8


def GetDynamodbClient(key_path="/home/lizhifeng/.ssh/landscape_cn_key",
                      region="cn-north-1",
                      endpoint='http://dynamodb.cn-north-1.amazonaws.com.cn'):

    key_fd = open(key_path)

    aws_access_key = key_fd.readline().strip('\n')
    aws_secret_key = key_fd.readline().strip('\n')

    session = Session(aws_access_key,
                      aws_secret_key,
                      region_name=region)

    client = session.client('dynamodb', endpoint_url=endpoint)

    return client
