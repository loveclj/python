import boto3
from boto3.session import Session

# Ffrom boto3.session import Session

key_path = "/home/lizhifeng/.ssh/.aws_key"
key_fd = open(key_path)

aws_access_key =  key_fd.readline().strip('\n')
aws_secret_key =  key_fd.readline().strip('\n')


session = Session(aws_access_key,
                  aws_secret_key,
                  region_name='cn-north-1')


client = session.client('dynamodb', endpoint_url='http://dynamodb.cn-north-1.amazonaws.com.cn')
#dynamodb = session.resource('dynamodb', endpoint_url='http://localhost:8000')

response = client.list_tables()

response["TableNames"][2] ="test"
print response
