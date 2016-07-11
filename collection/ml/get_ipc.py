__author__ = 'lizhifeng'

from aws4_signature import GetDynamodbClient
import time


def dynamdb_scan(client, table_name, field):

    ipc_list = []
    response = client.scan(TableName=table_name, ProjectionExpression=field)

    while response["Count"] != 0:

        items = response[u"Items"]
        for item in items:
            ipc_list.append(item[u"ipc"][u"S"])

        if "LastEvaluatedKey" not in response.keys():
            break

        last_key = response[u"LastEvaluatedKey"][u"ipc"][u"S"]
        last_key_json = {"ipc":{}}
        last_key_json[field][u"S"] = last_key

        response = client.scan(TableName=table_name, ProjectionExpression=field, ExclusiveStartKey=last_key_json)

    return ipc_list


if __name__ == "__main__":

    client = GetDynamodbClient()
    table_name = "patent_classification_ipc"
    field = "ipc"
    ipc_list = []
    ipc_list = dynamdb_scan(client, table_name, field)

    sorted_ipc_list = sorted(ipc_list)
    for ipc in sorted_ipc_list:
        print ipc
